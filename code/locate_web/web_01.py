import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# 定义一个driver的变量，用来接收实例化后的浏览器
dirver = webdriver.Chrome()
# 使用get方法，访问网址
dirver.get("https://www.bilibili.com")
# 找到输入框位置，输入紧张的小虫虫
dirver.find_element(By.CLASS_NAME, 'nav-search-input').send_keys("小紧张的虫虫")
# 找到搜索框点击搜索
dirver.find_element(By.CLASS_NAME, 'nav-search-btn').click()

time.sleep(5)
dirver.close()
