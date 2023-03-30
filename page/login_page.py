from base import base
from selenium.webdriver.common.by import By

class login_page(base):
    # 定位器
    quxiao_loc = (By.CLASS_NAME,"el-button el-button--default el-button--small")
    username_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div/input')
    password_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input')
    login_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/button')
    # 页面的动作


