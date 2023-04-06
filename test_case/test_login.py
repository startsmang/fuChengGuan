import pytest
from selenium.webdriver.common.by import By

from base.base import PageBase
from config import config
from page.login_page import login_page

class Test_login(login_page):
    def setup(self):
        self.login_page = login_page()
    def teardown(self):
        # self.login_page.quit()
        pass



def test_login_fuChengGuan1():
        p1 = login_page()
        p1.login()



if __name__ == '__main__':
    pytest.main(["-vs", "test_login.py"])



