
# coding=utf-8
from calculator import Count
import unittest
# 单元测试用例

class TestAdd(unittest.TestCase):

# 初始化测试环境

    def setUp(self):
        print ("test case start")

# 清除产生的数据

    def tearDown(self):
        print ("test case end")

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

if __name__ == 'main':
    unittest.main()
