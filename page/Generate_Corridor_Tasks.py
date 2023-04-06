from time import sleep
from selenium import webdriver
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
from base.base import PageBase
from page.login_page import login_page


class Generate_Corridor_Tasks_Page(PageBase):
    # 定位器
    #点击取消
    quxiao_loc = (By.XPATH , "/html/body/div[2]/div/div[1]/button/i")
    #输入用户名
    username_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div/input')
    #输入密码
    password_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input')
    #点击登录
    login_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/button')
    #断言
    assert_loc = (By.XPATH , '//*[@id="app"]/div/div[2]/div/div/div[5]/span')

    #点击全部应用
    apply_loc = (By.XPATH , '//div[starts-with(@class,"Application hamburger-container")]')
    #点击环卫管理
    Sanitation_loc = (By.XPATH ,'//p[starts-with(@text,"环卫作业")]')
    #点击道路保洁任务
    roadr_Tasks_loc = (By.XPATH , '//div[starts-with(@style,"padding-left: 40px; color: rgb(133, 144, 165); background-color: rgb(37, 43, 59);")]')
    #点击生成道路保洁任务
    create_road_loc = (By.XPATH , '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[12]/li/ul/div[2]/li/ul/div[2]/a/li')

    def login(self):
        self.open_browser()
        sleep(1)
        self.locator_element(Generate_Corridor_Tasks_Page.quxiao_loc).click()
        sleep(1)
        self.send_keys(Generate_Corridor_Tasks_Page.username_loc,"admin")

        self.send_keys(Generate_Corridor_Tasks_Page.password_loc,"FJzx@2019.")

        self.click(Generate_Corridor_Tasks_Page.login_loc)
        sleep(5)
        #断言
        self.assert_texdt = self.locator_element(Generate_Corridor_Tasks_Page.assert_loc).text
        print(type(self.assert_texdt))
        print(self.assert_texdt)

        if self.assert_texdt in "超级管理员,您好":
            print("登录成功")
        else:
            print("登录失败")
        self.assert_texdt = self.locator_element(login_page.assert_loc).text
    def create_road(self):

        self.click(Generate_Corridor_Tasks_Page.apply_loc)
        sleep(1)
        self.click(Generate_Corridor_Tasks_Page.Sanitation_loc)
        sleep(2)
        self.click(Generate_Corridor_Tasks_Page.roadr_Tasks_loc)
        sleep(2)
        self.click(Generate_Corridor_Tasks_Page.create_road_loc)
        sleep(3)

    def quit(self):
        self.driver.quit()
