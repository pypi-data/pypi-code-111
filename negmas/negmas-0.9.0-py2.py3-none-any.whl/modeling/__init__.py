# -*- coding: utf-8 -*-
"""A package for generalized opponent modeling"""
from __future__ import annotations

from .acceptance import *
from .future import *
from .strategy import *
from .utility import *

__all__ = acceptance.__all__ + strategy.__all__ + utility.__all__ + future.__all__
