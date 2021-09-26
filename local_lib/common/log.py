#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : log.py
import logging
import os
import time


class Log(object):

    def __init__(self, filename):
        self.filename = os.path.join(filename, '{0}.log'.format(time.strftime('%Y-%m-%d')))

    def __out_print(self, level, message):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        fh = logging.FileHandler(self.filename, 'a', encoding='UTF8')
        fh.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == 'debug':
            if not isinstance(message, str):
                message = str(message)
            logger.debug(message)

        if level == 'info':
            if not isinstance(message, str):
                message = str(message)
            logger.info(message)

        if level == 'warning':
            if not isinstance(message, str):
                message = str(message)
            logger.warning(message)

        if level == 'error':
            if not isinstance(message, str):
                message = str(message)
            logger.error(message)

        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, message):
        self.__out_print('debug', message)

    def info(self, message):
        self.__out_print('info', message)

    def warning(self, message):
        self.__out_print('warning', message)

    def error(self, message):
        self.__out_print('error', message)

if __name__ == '__main__':
    a = 'C:\\Users\\zmz\\Desktop\\test-tb-jenkins\\log'
    log=Log(a)
    log.debug('我是你爹')