#! /usr/python/bin
# -*- coding=UTF-8 -*-

import unittest
import HTMLTestRunnerCN
import os
test = os.getcwd()
print(test)
caselist = test  +"\\firefox_test"
print(caselist)

if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    discover = unittest.defaultTestLoader.discover(caselist,pattern='test*.py',top_level_dir=None)
#    test_suite.addTest(domo('test_run1'))  # 测试套件中添加测试用例
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    fp = open('./firefox_test/Repost/test.html', 'wb')  # 打开一个保存结果的html文件
    runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title=u'api测试报告', description=u'测试情况')
    # 生成执行用例的对象
    runner.run(discover)
    # 执行测试套件