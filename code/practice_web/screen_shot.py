import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utils.get_filepath import get_screen_shot_path


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://news.baidu.com/")
driver.implicitly_wait(3)
element = driver.find_elements(By.XPATH, "//a[contains(text(),'财经')]")[3]

# scrollIntoView将元素定位在可视范围内
driver.execute_script("arguments[0].scrollIntoView();", element)
# 截屏
driver.save_screenshot(get_screen_shot_path())
time.sleep(3)
driver.close()