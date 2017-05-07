# coding=utf-8
import unittest
import time
# 导入参数-测试模块类中的函数
import testadd
import testsub
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 构造测试集

suite = unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))

suite.addTest(testsub.TestAdd("test_sub"))
suite.addTest(testsub.TestAdd("test_sub2"))

if __name__ == '__main__':

    # 定义报告存放路径
    fp = open('./ result.html', 'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')

    # 测试执行
    # runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()

