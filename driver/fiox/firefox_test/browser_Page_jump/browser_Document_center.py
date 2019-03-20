#encoding:utf-8
'''
@author: guanyf
@contact:guanyf3@lenovo.com
@tel :18837121280
'''
'''
##############################
#                             #
#    文档中心 -->目前目镜      #
#    为开发者路径--后续修改    #
#                            #
#############################
'''
from selenium import webdriver
import time
import unittest
from ..data import *
class browser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        # 跳转页面  --》开发者路径
        self.driver.find_element_by_xpath(Bro_dev_Center).click()
        time.sleep(2)
        #进入页面 https://siotdev.lenovo.com.cn/developers
        self.driver.switch_to_window(self.driver.window_handles[1])
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()