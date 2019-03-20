# encoding: utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
'''
##############################
#                             #
#通过开发者中心，登录到注册页面#
#                            #
#############################
'''
from browser_Page_jump import browser_developer_center
import time
import data
class test_registered_mail(browser_developer_center.test_center):
    def test_mail(self):
        self.driver.find_element_by_xpath(data.registered_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(data.mail_button).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(data.mail_input).clear()
        self.driver.find_element_by_xpath(data.mail_input).send_keys("123456789@gyf.com")
        time.sleep(2)
        text = self.driver.find_element_by_xpath(data.mail_input).text
        print(text)