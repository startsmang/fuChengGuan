import pytest
from selenium.webdriver.common.by import By

from base.base import PageBase
from config import config
from page.login_page import login_page
class test_login(login_page):
    def __init__(self):
        login_page.__init__(self)
        PageBase.__init__(self)
        super().__init__()

def test_login_fuChengGuan1():
        p1 = login_page()
        p1.test_login_fuChengGuan()



if __name__ == '__main__':
    pytest.main(["-vs", "test_login.py"])



