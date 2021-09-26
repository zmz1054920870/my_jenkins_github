#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : write_config.py
import traceback
from configparser import ConfigParser


class WriteConfig(object):

    def __init__(self, filename):
        self.filename = filename

    def write_config(self, section, option, value):
        try:
            config = ConfigParser()
            config.read(self.filename, encoding='UTF8')
            if section not in config.sections():
                config.add_section(section)
            config.set(section, option, value)
            with open(self.filename, 'w') as f:
                config.write(f)
        except Exception as e:
            print(e)