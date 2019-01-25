#coding=utf-8
import unittest, doctest
from XBT import test_xbt
import HTMLTestRunner

suite = doctest.DocTestSuite()
#罗列要执行的文件
suite.addTest(unittest.makeSuite(test_xbt.XBT))
# suite.addTest(unittest.makeSuite(test_youdao.Youdao))

filename = 'D:\\pycharm_project\\webtest\\Report\\result_xbt.html'  # 定义个报告存放路径，支持相对路径。
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Report_title',
    description='Report_description')
runner.run(suite)  # 自动进行测试
fp.close()
