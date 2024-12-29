import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://iviewui.com/view-ui-plus/component/form/date-picker")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@class='ivu-input ivu-input-default ivu-input-with-suffix']").send_keys("2024-08-08")
driver.find_elements(By.XPATH, "//input[@class='ivu-input ivu-input-default ivu-input-with-suffix']")[1].send_keys("2024-08-06 - 2024-09-19")


time.sleep(3)
driver.close()