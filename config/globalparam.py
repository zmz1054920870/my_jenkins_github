#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : globalparam.py
import os
from local_lib.common.log import Log
from local_lib.common.utils.write_config import WriteConfig
from local_lib.common.utils.read_config import ReadConfig


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(project_path, 'log')
config_path = os.path.join(project_path, 'config', 'config.ini')


log = Log(log_path)
write_config = WriteConfig(config_path).write_config
read_config = ReadConfig(config_path).read_config
