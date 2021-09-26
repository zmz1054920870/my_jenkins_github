#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2021/3/25 23:53
# @Author  : 超级无敌张铁柱
# @File    : conftest.py
# conftest.py
import pytest
import time

def pytest_configure(config):
    mark_list = ['blocker', 'critical', 'normal', 'minor', 'trivial']
    for marks in mark_list:
        config.addinivalue_line('markers', marks)


# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     print('------------------------------------')
#     # 获取钩子方法的调用结果
#     out = yield
#     print('用例执行结果', out)  # <pluggy.callers._Result object at 0x000001CC4ECFB908>
#
#     # 3. 从钩子方法的调用结果中获取测试报告
#     report = out.get_result()
#     print('用例对象', item)  # <Function test_inter_sub_one>
#     print('测试报告：%s' % report)  # <Function test_inter_sub_four>
#     print('report对象属性', report.__dict__)
#     """
#     {'nodeid': 'test_inter.py::TestInter::test_inter_sub_one', 'location': ('test_inter.py', 12, 'TestInter.test_inter_sub_one'), 'keywords': {'test_inter_sub_one': 1, '()': 1, '接口脚本': 1, 'test_inter.py': 1, 'TestInter': 1}, 'outcome': 'passed', 'longrepr': None, 'when': 'call', 'user_properties': [], 'sections': [], 'duration': 0.0}
#     """
#
#     print('步骤：%s' % report.when)  # call
#     print('nodeid：%s' % report.nodeid)  # D:/interface/接口测试/test_inter.py::TestInter::test_inter_sub_one
#     print('测试用例函数', item.function)  # <function TestInter.test_inter_sub_one at 0x0000014C14A236A8>
#     print('description:%s' % str(item.function.__doc__))  # 这是一段多行注释
#     print(('运行结果: %s' % report.outcome))  # passed
#     print('3', item.session.__dict__)
#     """
#     {'fspath': local('D:\\origin\\学习代码\\interface_auto\\src\\api_case'), 'name': 'api_case', 'parent': None, 'config': <_pytest.config.Config object at 0x000001F6EA6C4EB8>, 'session': <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>, 'keywords': <NodeKeywords for node <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>>, 'own_markers': [], 'extra_keyword_matches': set(), '_name2pseudofixturedef': {}, '_nodeid': '', 'testsfailed': 0, 'testscollected': 7, 'shouldstop': False, 'shouldfail': False, 'trace': <pluggy._tracing.TagTracerSub object at 0x000001F6EB755550>, '_norecursepatterns': ['.*', 'build', 'dist', 'CVS', '_darcs', '{arch}', '*.egg', 'venv'], 'startdir': local('D:\\origin\\学习代码\\interface_auto\\src\\api_case'), '_initialpaths': frozenset({local('D:\\origin\\学习代码\\interface_auto\\src\\api_case')}), '_node_cache': {local('D:\\origin\\学习代码\\interface_auto\\src\\__init__.py'): [<Package D:\origin\学习代码\interface_auto\src>], (<class '_pytest.python.Module'>, local('D:\\origin\\学习代码\\interface_auto\\src\\api_case\\接口脚本\\test_inter.py')): <Module 接口脚本/test_inter.py>, (<class '_pytest.python.Module'>, local('D:\\origin\\学习代码\\interface_auto\\src\\api_case\\接口脚本\\test_inter_two.py')): <Module 接口脚本/test_inter_two.py>}, '_bestrelpathcache': _bestrelpath_cache(path=local('D:\\origin\\学习代码\\interface_auto\\src\\api_case')), '_pkg_roots': {local('D:\\origin\\学习代码\\interface_auto\\src'): <Package D:\origin\学习代码\interface_auto\src>, local('D:\\origin\\学习代码\\interface_auto\\src\\api_case\\演示脚本'): <Package D:\origin\学习代码\interface_auto\src\api_case\演示脚本>}, 'exitstatus': <ExitCode.OK: 0>, '_fixturemanager': <_pytest.fixtures.FixtureManager object at 0x000001F6EB755240>, '_setupstate': <_pytest.runner.SetupState object at 0x000001F6EB773400>, '_notfound': [], '_initialparts': [[local('D:\\origin\\学习代码\\interface_auto\\src\\api_case')]], 'items': [<Function test_inter_sub_one>, <Function test_inter_sub_two>, <Function test_inter_sub_three>, <Function test_inter_sub_four>, <Function test_inter_sub_five>, <Function test_inter_sub_six>, <Function test_demo_sub_two>]}
#     """
#     print('4', item.config)  # <_pytest.config.Config object at 0x000001F6EA6C4EB8>
#     print('5', item.parent)  # <Instance ()>
#     print('6', item.nodeid)  # 接口脚本/test_inter.py::TestInter::test_inter_sub_one (命名， 我们可以修改，他的命名， 也可以修改ids中文的问题)
#     print('7', item.session.items)
#     """
#    [<Function test_inter_sub_one>, <Function test_inter_sub_two>, <Function test_inter_sub_three>, <Function test_inter_sub_four>]
#     """
#
#     print('8', item.session.items[0].__dict__)
#     """
#     {'name': 'test_inter_sub_one', 'parent': <Instance ()>, 'config': <_pytest.config.Config object at 0x000001F6EA6C4EB8>, 'session': <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>, 'fspath': local('D:\\origin\\学习代码\\interface_auto\\src\\api_case\\接口脚本\\test_inter.py'), 'keywords': <NodeKeywords for node <Function test_inter_sub_one>>, 'own_markers': [], 'extra_keyword_matches': set(), '_name2pseudofixturedef': {}, '_nodeid': '接口脚本/test_inter.py::TestInter::test_inter_sub_one', '_report_sections': [], 'user_properties': [], '_args': None, '_obj': <bound method TestInter.test_inter_sub_one of <test_inter.TestInter object at 0x000001F6EB7C5F98>>, '_fixtureinfo': FuncFixtureInfo(argnames=(), initialnames=('_session_faker',), names_closure=['_session_faker', 'request'], name2fixturedefs={'_session_faker': (<FixtureDef argname='_session_faker' scope='session' baseid=''>,)}), 'fixturenames': ['_session_faker', 'request'], 'funcargs': {'_session_faker': <faker.proxy.Faker object at 0x000001F6EB7C5EB8>, 'request': <FixtureRequest for <Function test_inter_sub_one>>}, '_request': <FixtureRequest for <Function test_inter_sub_one>>, 'originalname': None, '_location': ('接口脚本\\test_inter.py', 12, 'TestInter.test_inter_sub_one'), 'catch_log_handlers': {'setup': <LogCaptureHandler (NOTSET)>, 'call': <LogCaptureHandler (NOTSET)>}, 'catch_log_handler': <LogCaptureHandler (NOTSET)>, '_skipped_by_mark': False, '_evalxfail': <_pytest.mark.evaluate.MarkEvaluator object at 0x000001F6EB7C5F60>}
#     """
#
#     print('9', item.session)  # <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>
#     print('10', item.session.items[
#         0].session)  # <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>
#
#     print('11', item.__dict__)  # item.__dict__ == item.session.items[0].__dict__
#     """
#     {'name': 'test_inter_sub_one', 'parent': <Instance ()>, 'config': <_pytest.config.Config object at 0x000001F6EA6C4EB8>, 'session': <Session api_case exitstatus=<ExitCode.OK: 0> testsfailed=0 testscollected=7>, 'fspath': local('D:\\origin\\学习代码\\interface_auto\\src\\api_case\\接口脚本\\test_inter.py'), 'keywords': <NodeKeywords for node <Function test_inter_sub_one>>, 'own_markers': [], 'extra_keyword_matches': set(), '_name2pseudofixturedef': {}, '_nodeid': '接口脚本/test_inter.py::TestInter::test_inter_sub_one', '_report_sections': [], 'user_properties': [], '_args': None, '_obj': <bound method TestInter.test_inter_sub_one of <test_inter.TestInter object at 0x000001F6EB7C5F98>>, '_fixtureinfo': FuncFixtureInfo(argnames=(), initialnames=('_session_faker',), names_closure=['_session_faker', 'request'], name2fixturedefs={'_session_faker': (<FixtureDef argname='_session_faker' scope='session' baseid=''>,)}), 'fixturenames': ['_session_faker', 'request'], 'funcargs': {'_session_faker': <faker.proxy.Faker object at 0x000001F6EB7C5EB8>, 'request': <FixtureRequest for <Function test_inter_sub_one>>}, '_request': <FixtureRequest for <Function test_inter_sub_one>>, 'originalname': None, '_location': ('接口脚本\\test_inter.py', 12, 'TestInter.test_inter_sub_one'), 'catch_log_handlers': {'setup': <LogCaptureHandler (NOTSET)>, 'call': <LogCaptureHandler (NOTSET)>}, 'catch_log_handler': <LogCaptureHandler (NOTSET)>, '_skipped_by_mark': False, '_evalxfail': <_pytest.mark.evaluate.MarkEvaluator object at 0x000001F6EB7C5F60>}
#
#     """
#
#     print('12', dir(item))
#     """
#     ['_ALLOW_MARKERS', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_args', '_evalxfail', '_fixtureinfo', '_getobj', '_initrequest', '_location', '_name2pseudofixturedef', '_nodeid', '_obj', '_prunetraceback', '_pyfuncitem', '_report_sections', '_repr_failure_py', '_request', '_skipped_by_mark', 'add_marker', 'add_report_section', 'addfinalizer', 'catch_log_handler', 'catch_log_handlers', 'cls', 'config', 'extra_keyword_matches', 'fixturenames', 'fspath', 'funcargnames', 'funcargs', 'function', 'get_closest_marker', 'getmodpath', 'getparent', 'ihook', 'instance', 'iter_markers', 'iter_markers_with_node', 'keywords', 'listchain', 'listextrakeywords', 'listnames', 'location', 'module', 'name', 'nextitem', 'nodeid', 'obj', 'originalname', 'own_markers', 'parent', 'reportinfo', 'repr_failure', 'runtest', 'session', 'setup', 'teardown', 'user_properties', 'warn']

