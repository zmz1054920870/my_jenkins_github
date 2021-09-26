#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : test_3.py
import pytest
import os
import allure


# @pytest.fixture(scope='class', params=['zhangsan', 'lisi'], ids=['xxx', 'yyy'], autouse=True)
# def input_user(request):
#     print(1111111111111111111111111)
#     return request.param

def setup_module():
    with allure.step('构建测试数据'):
        print('\033[1;35m setup_module setup_module setup_module setup_module setup_module \033[0m')


def teardown_module():
    with allure.step('清除测试数据'):
        print('\033[1;35m teardown_module teardown_module teardown_module teardown_module \033[0m')


@pytest.fixture(params=['1+1', '2+2', '3+3'], ids=['num_one1', 'num_two1', 'num_three'])
def input_string(request):
    return request.param


@pytest.fixture(params=[2, 4, 6], ids=['expect_one', 'expect_two', 'expect_three'])
def expected(request):
    return request.param


@allure.feature('问答通用设置')
@allure.story('特殊前缀')
class TestCase3(object):

    def setup_class(self):
        with allure.step('登录'):
            print('\033[1;35m ------------------------------------------------- \033[0m')

    def teardown_class(self):
        with allure.step('登出'):
            print('\033[1;35m ================================================== \033[0m')

    @allure.title('问答通用设置 - 特殊前缀 - 开关打开校验')
    @allure.severity('critical')
    @pytest.mark.critical
    def test_case_3_one_true(self):
        with allure.step('第一步: 打开特殊前置开关'):
            print('\033[1;32m test_case_3_one_true %s \n \033[0m')
        with allure.step('第二步: 进行机器人问答'):
            print('\033[1;32m test_case_3_one_true %s \n \033[0m')
        with allure.step('第三步: 校验结果'):
            print('\033[1;32m test_case_3_one_true %s \n \033[0m')

    @allure.title('问答通用设置 - 特殊前缀 - 开关关闭校验')
    @allure.severity('normal')
    @allure.testcase('https://www.baidu.com', '用例2573')
    @allure.issue('http://39.101.244.16:8080/', 'bug-01')
    def test_case_3_three_true(self, input_string, expected):
        with allure.step('第一步: 关闭特殊前缀开关'):
            print('\033[1;32m test_case_3_three_true\n \033[0m')
        with allure.step('第二步: 进行机器人问答'):
            print('\033[1;32m test_case_3_three_true\n \033[0m')
        with allure.step('第三步: 校验结果'):
            assert eval(input_string) == expected

    @pytest.mark.parametrize(
        'AA, BB',
        [
            pytest.param('1+1', 2, id='num_one, expect_one'),
            pytest.param('2+2', 4, id='num_one_2, expect_one_2')
            # pytest.param('2+2', 4, pytest.mark.)
        ]
    )
    @allure.title('问答通用设置 - 特殊前缀 - 特殊字符校验')
    @allure.severity('minor')
    @allure.testcase('https://www.baidu.com', 'case111111111111111111')
    @pytest.mark.minor
    def test_case_3_two_true(self, AA, BB):
        # print('\033[1;35m test_inter_two_sub_three \033[0m')
        # print('\033[1;36m %s : %s \033[0m' % (input_user, input_pwd))
        with allure.step('第一步:打开开关'):
            print('\033[1;32m test_case_3_two_true %s \n \033[0m')
        with allure.step('第二步:输入特殊字符'):
            print('\033[1;32m test_case_3_two_true %s \n \033[0m')
        with allure.step('第三步:进行校验'):
            print('\033[1;32m test_case_3_two_true %s \n \033[0m')
        assert 1
        with allure.step('讲演结果'):
            assert 1


if __name__ == '__main__':
    pytest.main(['-s', '-v', '--alluredir=./report/raw_data', './test_3.py'])
    # pytest.main(['-s', '--collect-only'])
