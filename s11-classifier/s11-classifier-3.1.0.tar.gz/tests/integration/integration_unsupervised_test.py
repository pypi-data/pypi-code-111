"Unsupervised classification test for classifier"
from pathlib import Path

import numpy as np
import pytest
import rasterio
from classifier.cli import classification
from classifier.settings import WORKSPACE
from classifier.utils.general import save_config_as_json


@pytest.mark.parametrize('test_arg',
                         [[False, False]])
def test_unsupervised_kmeans(runner):
    """
    Test for running an unsupervised kmeans classification
    """
    save_config_as_json(threads=1, algorithm="us_kmeans")

    runner.invoke(classification, [
        "--name", 'test_result', '--overwrite', True,
        "integration_test_rasters"])
    directory = Path(WORKSPACE) / 'test_result' / 'classification.tif'
    with rasterio.open(directory, 'r') as dst:
        result = dst.read(1)
        assert np.all(result[:, 0:4] == result[0, 0])
        assert np.all(result[:, 5:10] == result[0, 5])


@pytest.mark.parametrize('test_arg',
                         [[False, False]])
def test_unsupervised_kmeans_minibatch(runner):
    """
    Test for running an unsupervised kmeans-minibatch classification
    """
    save_config_as_json(threads=1, algorithm="us_kmeans_minibatch")

    runner.invoke(classification, [
        "--name", 'test_result', '--overwrite', True,
        "integration_test_rasters"])
    directory = Path(WORKSPACE) / 'test_result' / 'classification.tif'
    with rasterio.open(directory, 'r') as dst:
        result = dst.read(1)
        assert np.all(result[:, 0:4] == result[0, 0])
        assert np.all(result[:, 5:10] == result[0, 5])
