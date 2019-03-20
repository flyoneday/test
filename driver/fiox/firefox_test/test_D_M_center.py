# encoding: utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
import time
import data
from browser_Page_jump import browser_developer_center
class test_D_M_center(browser_developer_center.test_center):
    def test_registered(self):
        # /html/body/div[1]/div/div[3]/p[3]/a  注册路径
        self.driver.find_element_by_xpath(data.registered_button).click()
        time.sleep(2)
        registered02 = self.driver.find_element_by_xpath(data.registered_tel).text
        registered03 = self.driver.current_url
        print(registered03)
#         try:
#            return registered03
#         finally:
        print registered02
        assert registered02 == u"手机号注册","fail"
        print u"通过文档中心，成功登录到注册页面"























        # print(self.setUp111())
        # self.driver.find_element_by_xpath("//*[@id='regiestBtn']")
