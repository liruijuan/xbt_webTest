#coding=utf-8
import unittest, doctest
from XBT import test_xbt,web_unit
import HTMLTestRunner
from Configure import configures

suite = doctest.DocTestSuite()
#罗列要执行的文件
suite.addTest(unittest.makeSuite(test_xbt.XBT))
suite.addTest(unittest.makeSuite(web_unit.Baidu))

filename = configures.REPORT_FILE # 定义个报告存放路径，支持相对路径。
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='Report_title',
    description='Report_description')
runner.run(suite)  # 自动进行测试
fp.close()
