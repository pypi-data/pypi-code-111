import numpy as np


class GlobalAveragePool:
    def __init__(self, opset_version, **kwargs):
        self.version = opset_version

    def run(self, x):
        return [np.mean(x, axis=tuple(range(2, np.ndim(x))), keepdims=True)]
