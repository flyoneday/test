# encoding: utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
import time
import data
from browser_Page_jump import browser_Document_center
class  test_login(browser_Document_center.browser):
    def test_login01(self):
        registered01 = self.driver.find_element_by_xpath(data.registered_button).text
        assert registered01 == u"注册","fail"
        print u"成功登录到带有注册的页面"
        
    def test_registered01(self):
        self.driver.find_element_by_xpath(data.registered_button).click()
        time.sleep(2)
        registered02 = self.driver.find_element_by_xpath(data.registered_tel).text
        print(registered02)
        assert registered02 == u"手机号注册","fail"
        print u"成功登录到注册页面"