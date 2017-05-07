#coding=utf-8

"""
@Author:Lq
@Date:2017-04-30
"""

class Login():

#登录函数
    def user_login(self, driver, username, password):
        driver.find_element_by_id("userPhone").clear()
        driver.find_element_by_id("userPhone").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath('//*[@id="login"]').click()

#首页
    def homepage(self, driver):
        driver.find_element_by_class_name("w-me").click()

#个人中心页
    def personal(self, driver):
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[1]').click()

#退出函数
    def user_logout(self, driver):
        driver.find_element_by_class_name("btn").click()
        driver.quit()




