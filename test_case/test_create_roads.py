import pytest
from selenium.webdriver.common.by import By
from time import sleep
from base.base import PageBase
from config import config
from page.login_page import login_page
from page.Generate_Corridor_Tasks import Generate_Corridor_Tasks_Page
class Test_Generate_Corridor_Tasks(Generate_Corridor_Tasks_Page):
    pass

def test_create_roads():
        p1 = Generate_Corridor_Tasks_Page()
        p1.test_create_road()

if __name__ == '__main__':
    pytest.main(["-vs", "test_create_roads.py"])