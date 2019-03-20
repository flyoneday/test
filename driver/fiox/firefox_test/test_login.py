from selenium import webdriver
from time import sleep
def test_1(func):
    def test(*args, **kwargs):
        driver = webdriver.Firefox()
        driver.get('https://siotdev.lenovo.com.cn')
        sleep(4)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/div/a").click()
        sleep(4)
        driver.find_element_by_xpath("/html/body/div[2]/div/p[3]/a").click()
        sleep(4)
        driver.find_element_by_xpath("//input[@id='tuser']").send_keys("986118772@qq.com")
        driver.find_element_by_xpath("//*[@id='tpass']").send_keys("zxcvbnm...")
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/form[1]/div/div[2]/div[4]/div[1]/input").click()
        sleep(4)
        return func(*args, **kwargs)
    return test
