import pytest
from base.base import base
from config import config
from page.login_page import login_page
class Test_login(login_page):

    def open_browser(self):
        self.driver = config.config()
        self.driver.get("https://jxh.zx1026.com/")
        self.driver.maximize_window()
    def click_quxiao(self):
            self.locator_element(login_page.quxiao_loc)
    def send_username(self):
            self.locator_element(login_page.username_loc).
    def send_password(self):
            self.send_keys(login_page.password_loc, "FJzx@2019.")
    def click_button(self):
            self.click(login_page.login_loc)

if __name__ == '__main__':
    pytest.main(["-vs", "test_login.py"])



