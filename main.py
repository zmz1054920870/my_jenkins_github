#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : main.py
import pytest

pytest.main(['-s', '-v', '--reruns=1', '--html=./report.html'])