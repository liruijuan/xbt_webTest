#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
from Configure import configures


class XBT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://18.136.200.245:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    #新巴特官网用例
    def test_xbt_search(self):
        u"""新巴特网站用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
            driver.find_element_by_link_text("首页").click()
        except:
            driver.get_screenshot_as_file(configures.ERROT_PNG_PATH + "xbt1.png")
            #如果没有找到上面的元素就截取当前页面。
        try:
            driver.get(self.base_url + "/chanpina")
            driver.get(self.base_url + "/chanpinb")
        except:
            driver.get_screenshot_as_file(configures.ERROT_PNG_PATH + "xbt2.png")
            #如果没有找到上面的元素就截取当前页面。
        try:
            driver.get(self.base_url + "/guanyu")
            driver.get(self.base_url + "/tuandui")
            driver.get(self.base_url + "/add")
        except:
            driver.get_screenshot_as_file(configures.ERROT_PNG_PATH + "xbt3.png")
            # 如果没有找到上面的元素就截取当前页面。
        try:
            driver.get(self.base_url + "/recruitment")
        except:
            driver.get_screenshot_as_file(configures.ERROT_PNG_PATH + "xbt4.png")
            # 如果没有找到上面的元素就截取当前页面。

        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(XBT("test_xbt_search"))
    #同样的，可以在这个文件中添加更多的用例。
    #suite.addTest(Youdao("aaaa"))
    results = unittest.TextTestRunner().run(suite)