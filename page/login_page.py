import time

from base.base import PageBase
from selenium.webdriver.common.by import By

class login_page(PageBase):
    # 定位器
    quxiao_loc = (By.XPATH , "/html/body/div[2]/div/div[1]/button/i")
    username_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div/input')
    password_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input')
    login_loc = (By.XPATH , '//*[@id="app"]/div/section[2]/form[1]/button')
    assert_loc = (By.XPATH , '//*[@id="app"]/div/div[2]/div/div/div[5]/span')
    # 页面的动作
    def login(self):
        self.open_browser()
        time.sleep(1)
        self.locator_element(login_page.quxiao_loc).click()
        time.sleep(1)
        self.send_keys(login_page.username_loc,"admin")

        self.send_keys(login_page.password_loc,"FJzx@2019.")

        self.click(login_page.login_loc)
        time.sleep(5)
        self.assert_texdt = self.locator_element(login_page.assert_loc).text

    def assert_01(self):
            if self.assert_texdt in "超级管理员":
                print("登录成功")
            else:
                print("登录失败")
    # def quit(self):
    #     self.driver.quit()




