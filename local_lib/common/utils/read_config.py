#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : read_config.py
from configparser import ConfigParser


class ReadConfig(object):

    def __init__(self, filename):
        self.filename = filename

    def read_config(self, section, option):
        config = ConfigParser()
        config.read(self.filename, encoding='UTF8')
        try:
            value = config.read(section, option)
            print(config.items('PORT'))
            return value
        except Exception as e:
            print(e)