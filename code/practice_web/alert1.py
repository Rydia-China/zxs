import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://sahitest.com/demo/alertTest.htm")
# driver.get("https://sahitest.com/demo/confirmTest.htm")
driver.get("https://sahitest.com/demo/promptTest.htm")
driver.maximize_window()

# alter弹框演示
# driver.find_element(By.NAME, "b1").click()
# 使用alter.text获取弹框的文字
# print(driver.switch_to.alert.text)
# 使用alter.accept() 点击确定
# driver.switch_to.alert.accept()
# time.sleep(3)
# driver.close()

# confirm弹框演示
driver.find_element(By.NAME, "b1").click()
# 使用alter.text获取弹框的文字
print(driver.switch_to.alert.text)
# 点击同意
# driver.switch_to.alert.accept()
# 点击取消
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.close()


# prompt弹框演示
driver.find_element(By.NAME, "b1").click()
time.sleep(1)
# switch_to.alert.send_key输入内容
driver.switch_to.alert.send_keys("我同意")
# 点击同意
# driver.switch_to.alert.accept()
# 点击取消
driver.switch_to.alert.dismiss()
time.sleep(3)
driver.close()
