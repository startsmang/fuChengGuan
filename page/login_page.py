from base.base import PageBase
from selenium.webdriver.common.by import By

class login_page(PageBase):
    # 定位器
    quxiao_loc = (By.XPATH,"/html/body/div[2]/div/div[3]/button[1]")
    username_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[1]/div/div/input')
    password_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/div[2]/div/div/input')
    login_loc = (By.XPATH,'//*[@id="app"]/div/section[2]/form[1]/button')
    # 页面的动作
    def test_login_fuChengGuan(self):
        self.open_browser()
        self.locator_element(login_page.quxiao_loc)
        self.locator_element(login_page.username_loc).send_keys("admin")
        self.locator_element(login_page.password_loc).send_keys("FJzx@2019.")
        self.click(login_page.login_loc)


