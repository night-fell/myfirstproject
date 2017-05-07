# coding=utf-8

import unittest
from selenium import webdriver
from loginwecash import Login
import time
import HTMLTestRunner
import sys
reload(sys)
sys.setdefaultencoding('utf8')


class LoginTest ():
    def __init__(self):
        # 设置浏览器为手机模式
        mobileEmulation = {'deviceName': 'Apple iPhone 5'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileEmulation)
        # 生成web对象
        self.driver = webdriver.Chrome(chrome_options=options)
        # 打开指定URL
        self.driver.get("http://m.wecash.net/wep/user/login.html")

    def test_mynumber_login(self):
        # 调用登录模块,增加浏览器驱动入参
        username = '15110185703'
        password = '1q2w3e'
        Login().user_login(self.driver, username, password)
        time.sleep(5)

        Login().homepage(self.driver)
        time.sleep(5)

        Login().personal(self.driver)
        time.sleep(5)
        # 调用退出模块
        Login().user_logout(self.driver)

  # 其他账号登录
    def test_other_login(self):
        username = '17744441116'
        password = '123456'
        Login().user_login(self.driver, username, password)
        time.sleep(5)

        Login().homepage(self.driver)
        time.sleep(5)

        Login().personal(self.driver)
        time.sleep(5)

        Login().user_logout(self.driver)


LoginTest().test_mynumber_login()
LoginTest().test_other_login()



