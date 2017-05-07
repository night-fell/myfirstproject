# coding:utf-8
import unittest


class IntegerArithmeticTestCase(unittest.TestCase):

    def testAdd(self):
        self.assertEqual((1 + 2),3)
        self.assertEqual(1 + 0, 1)

    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)

    def testMinus(self):
        u'''这里是测试减法'''
        result = 6-5
        hope = 1
        self.assertEqual(result, hope)

    def testDivide(self):
        u'''这里是测试除法'''
        result = 7/2
        hope = 3.5
        self.assertEqual(result, hope)


    if __name__ == '__main__':
        unittest.main()



