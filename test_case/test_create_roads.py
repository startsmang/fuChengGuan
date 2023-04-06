import pytest
from selenium.webdriver.common.by import By
from time import sleep
from base.base import PageBase
from config import config
from page.login_page import login_page
from page.Generate_Corridor_Tasks import Generate_Corridor_Tasks_Page
class Test_Generate_Corridor_Tasks(Generate_Corridor_Tasks_Page):
    # def setup(self):
    #     self.Generate_Corridor_Tasks_Page = Generate_Corridor_Tasks_Page()
    # def teardown(self):
    #     self.Generate_Corridor_Tasks_Page.quit()
    pass
@pytest.mark.run(order=1)
def test_login_fuChengGuan():
    p1 = Generate_Corridor_Tasks_Page()
    p1.login()
    p1.create_road()


if __name__ == '__main__':
    pytest.main(["--vs"])