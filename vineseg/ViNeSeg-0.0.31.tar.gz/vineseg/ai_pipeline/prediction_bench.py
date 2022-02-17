from .monai_models import get_model
from .DataLoader import DataReader
from .framework_bench import train, predict
from .add_channels import channelProcessingInput, channelProcessingOutput
from .preprocessing_augmentation import ( preprocessing
                                       , augmentation
                                       , convert_to_tensor
                                       )

from .postprocessing import postprocessing
from monai.losses import DiceLoss, FocalLoss, TverskyLoss
from monai.metrics import DiceMetric
from monai.utils import progress_bar
from monai.transforms import Compose
from torchcontrib.optim import SWA

import json
import torch
from typing import Tuple

def load_json_and_predict( path_load_folder: str
                         , path_image_folder: str
                         , path_masks: str
                         , device: str
                         , image_size: int
                         ) -> Tuple[dict, dict, list]:
    """
    Load all experiment paramter from json file to make a prediction.
    The user will get the prediction and the predictions metrics (if possible)
    Args:
        path_load_folder: string path from the json file
        path_image_folder: string path from images
        path_masks: string path to (potential) masks
        device: string Prediction on either gpu or cpu
        image_size: int input size of pictures for prediciton, we assume a quadratic picture
    Return:
        dict_predictions_default: dict  e.g {"image_name": np.array}
        dict_metrics_default: dict e.g {"average": None}
        list_file_paths: list Path to all images used for prediction
    """
    with open(path_load_folder + "Experiment_parameter.json") as File:
        dict_model_and_training = json.load(File)
        model_name = dict_model_and_training["model type"]
        input_channels = dict_model_and_training["number input channel"]
        output_channels = dict_model_and_training["number output channel"]
        image_size = dict_model_and_training.get('image_size_network', image_size)
        model = get_model( model_name
                         , input_channels
                         , output_channels
                         , device
                         , image_size
                         )
        swa_model = torch.optim.swa_utils.AveragedModel(model)
        path_model = path_load_folder + 'trained_weights/' + 'trained_weights.pth'
        path_swa_model = path_load_folder + 'trained_weights_swa/' + 'trained_weights.pth'
        model.load_state_dict(torch.load(path_model, map_location = device), strict=False)
        swa_model.load_state_dict(torch.load(path_swa_model, map_location = device), strict=True)
        channelManipulationOutput = dict_model_and_training["channel types output"]
        channelManipulationInput = dict_model_and_training["channel types input"]

    metric = DiceMetric( include_background = True
                       , reduction = "mean"
                       )
    _, val_recordings = DataReader( path_image_folder
                                  , path_masks
                                  , 1
                                  )
    data_val = [ { "img": channelProcessingInput(val_recordings[i].image, channelManipulationInput)
                 , "seg": channelProcessingOutput(val_recordings[i].label, channelManipulationOutput)
                 } for i in range(len(val_recordings))
               ]
    list_preprocessing_steps = preprocessing(dict_model_and_training["preprocessing steps"])
    postprocessing_steps = postprocessing(dict_model_and_training["postprocessing"])
    list_to_tensor = convert_to_tensor()
    trans_val = Compose(list_preprocessing_steps + list_to_tensor)
    list_data_names = [val_recordings[i].name for i in range(len(val_recordings))]
    list_file_paths = [val_recordings[i].filePath for i in range(len(val_recordings))] #neeed such that json is compatible to labelme
    dict_predictions_default, dict_metrics_default = predict( model #swa_model
                                                            , data_val
                                                            , trans_val
                                                            , list_data_names
                                                            , metric
                                                            , image_size
                                                            , postprocessing_steps
                                                            , device
                                                            )
    return dict_predictions_default, dict_metrics_default, list_file_paths
