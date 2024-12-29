from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage

# 存放页面定位元素
from utils.log_util import logger


class PageBaidu(BasePage):
    # 写成一个基类让PageBaidu继承,放在base_page
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()
    #     self.driver.get("https://www.baidu.com/")

    # 新闻
    news = (By.CSS_SELECTOR, "a[href='http://news.baidu.com']")
    # 百度一下按钮
    button = (By.ID, "su")
    # 百度输入框
    input = (By.ID, "kw")
    # 贴吧
    tieba = (By.CSS_SELECTOR, "a[href='http://tieba.baidu.com/']")
    # 帮助
    help = (By.CSS_SELECTOR, "a[href='//help.baidu.com']")
    # 更多
    more = (By.XPATH, "//*[@id='s-top-left']/div/a")

    # 将页面操作写成一个方法
    def search_keyword(self, keyword):
        logger.info("查找元素并输入内容")
        self.driver.find_element(*self.input).send_keys(keyword)
        logger.info("点击按钮")
        self.driver.find_element(*self.button).click()
