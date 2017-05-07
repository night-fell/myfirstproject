# coding:utf-8
from calculator import Count
import unittest

# 单元测试用例

class TestAdd(unittest.TestCase):
    def setUp(self):
        print ("test case1 start")

    def tearDown(self):
        print ("test case1 end")

    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        j = Count(71, 46)
        self.assertEqual(j.sub(), 25)


if __name__ == 'main':
    unittest.main()