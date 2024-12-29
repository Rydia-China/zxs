from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage

# 存放页面定位元素
from utils.log_util import logger


class PageSahi(BasePage):
    # 起始位置
    start = (By.ID, 'dragger')
    # 结束位置
    end = (By.XPATH, '/html/body/div[5]')
    # select
    select = (By.ID, "s1")
