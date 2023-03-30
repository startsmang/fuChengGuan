from selenium import webdriver
from selenium.webdriver.common.by import By
def config():
    driver = webdriver.Chrome()
    return driver