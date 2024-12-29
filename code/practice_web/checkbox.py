import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/checkbox")


# 根据文本定位
# driver.find_element(By.XPATH, "//span[text()='西瓜']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//span[text()='苹果']").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "//span[text()='香蕉']").click()
# time.sleep(3)
# driver.close()

# 根据同级哥哥定位
driver.find_element(By.XPATH, "//span[text()='西瓜']/preceding-sibling::span/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='苹果']/preceding-sibling::span/input").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[text()='香蕉']/preceding-sibling::span/input").click()
time.sleep(3)

driver.close()