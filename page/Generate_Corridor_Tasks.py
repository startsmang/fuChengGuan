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

class Generate_Corridor_Tasks_Page(PageBase,):
    def __init__(self):
        global driver
        self.driver = config.config()
        driver = self.driver
    # 定位器
    apply_loc = (By.XPATH , '//*[@id="app"]/div/div[2]/div/div/div[2]')
    Sanitation_loc = (By.XPATH , '//*[@id="app"]/div/div[2]/div/div/div[6]/div[1]/div[2]/div[3]/div')
    roadr_Tasks_loc = (By.XPATH , '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[12]/li/ul/div[2]/li/div')
    create_road_loc = (By.XPATH , '//*[@id="app"]/div/div[1]/div[2]/div[1]/div/ul/div[12]/li/ul/div[2]/li/ul/div[2]/a/li')

    def test_create_road(self):
        self.click(Generate_Corridor_Tasks_Page.apply_loc)
        sleep(1)
        self.click(Generate_Corridor_Tasks_Page.Sanitation_loc)
        sleep(2)
        self.click(Generate_Corridor_Tasks_Page.roadr_Tasks_loc)
        sleep(2)
        self.click(Generate_Corridor_Tasks_Page.create_road_loc)
        sleep(3)