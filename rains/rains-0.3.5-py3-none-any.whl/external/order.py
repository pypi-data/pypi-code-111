#!/usr/bin/env python3
# coding=UTF-8
#
# Copyright 2022. quinn.7@foxmail.com All rights reserved.
# Author :: cat7
# Email  :: quinn.7@foxmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""
[ 指令集 ]

"""

_MESSAGE = \
"""
--------------------------------------
 rains
--------------------------------------

 -init    | -i :: 初始化工程
 -make    | -m :: 创建项目
 -task    | -t :: 创建任务
 -run     | -r :: 运行任务文件或目录
 -server  | -s :: 运行服务器
 -help    | -h :: 查看帮助
 -version | -v :: 查看版本

--------------------------------------
"""


def function_order():
  """
  [ 指令集 ]
  
  """

  print(_MESSAGE)
