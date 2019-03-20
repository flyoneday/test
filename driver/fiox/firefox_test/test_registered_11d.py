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
import time
import data
from browser_Page_jump import browser_developer_center
class registered_11num(browser_developer_center.test_center):
    def test_registered11(self):
        # /html/body/div[1]/div/div[3]/p[3]/a  注册路径
        self.driver.find_element_by_xpath(data.registered_button).click()
        #手机号注册  /html/body/div[2]/div/div[1]/div[2]/span[1]/a     xpath
        pass1 = self.driver.find_element_by_xpath(data.registered_tel).text
        for i in range(0,10):
            self.driver.find_element_by_xpath(data.input_test).clear()
            if i <= 7:
                self.driver.find_element_by_xpath(data.input_test).send_keys("12345678901")
                assert pass1 == u"手机号注册", "fail"
                print u"11位码号测试通过"
                time.sleep(1)
            if i == 8:
                self.driver.find_element_by_xpath(data.input_test).send_keys("1234567890")
                time.sleep(1)
                assert pass1 == u"手机号注册", "fail"
                print u"少于11位码号测试通过"
            if i == 9:
                self.driver.find_element_by_xpath(data.input_test).send_keys("12345678901"+ str(i))
                time.sleep(1)
                assert pass1 == u"手机号注册", "fail"
                print u"大于11位码号测试通过"
            print("______________")

