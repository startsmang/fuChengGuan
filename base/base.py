import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from config import config
class PageBase():
    def __init__(self):
        global driver
        self.driver = config.config()
        driver = self.driver
# 封装一个方法，用于便捷的定位元素的关键词
    def locator_element(self,loc):
        return self.driver.find_element(*loc)

#  封装一个方法，用于便捷的定位到元素，并进行点击操作
    def click(self,loc):
        self.locator_element(loc).click()
#  封装一个方法，用于便捷的定位到元素，并进行输入操作
    def send_keys(self,loc,text):
        self.locator_element(loc).send_keys(text)
    def open_browser(self):
        self.driver.get('https://jxh.zx1026.com/')
        self.driver.maximize_window()
# 进入框架
    def goto_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)
# 退出框架
    def quit_frame(self):
        self.driver.switch_to.default_content()
# 封装选中下拉框
    def choice_select(self,loc,value):
         sel = Select(self.locator_element(loc))
         sel .select_by_value(value)

