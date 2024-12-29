import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://iviewui.com/view-ui-plus/component/form/cascader")

driver.find_element(By.XPATH, "//input[@class='ivu-input ivu-input-default']").click()
driver.find_element(By.XPATH, "//li[contains(text(),'北京')]").click()
driver.find_element(By.XPATH, "//li[contains(text(),'天坛')]").click()

time.sleep(3)
driver.close()