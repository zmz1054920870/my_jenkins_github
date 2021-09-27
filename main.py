#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : main.py
import pytest
import os
from config.globalparam import project_path
from local_lib.common.utils.send_email import EmailManage

report_path = os.path.join(project_path, 'report.html')
pytest.main(['-s', '-v', '--reruns=1', '--html=./report.html'])
EmailManage(report_path).send_email()