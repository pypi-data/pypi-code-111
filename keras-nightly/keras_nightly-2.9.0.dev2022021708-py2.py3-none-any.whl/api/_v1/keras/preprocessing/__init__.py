# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Provides keras data preprocessing utils to pre-process tf.data.Datasets before they are fed to the model.
"""

import sys as _sys

from keras.api._v1.keras.preprocessing import image
from keras.api._v1.keras.preprocessing import sequence
from keras.api._v1.keras.preprocessing import text
from tensorflow.python.util import module_wrapper as _module_wrapper

if not isinstance(_sys.modules[__name__], _module_wrapper.TFModuleWrapper):
  _sys.modules[__name__] = _module_wrapper.TFModuleWrapper(
      _sys.modules[__name__], "keras.preprocessing", public_apis=None, deprecation=True,
      has_lite=False)
