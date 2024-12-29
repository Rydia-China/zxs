import time
from pywinauto import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.iviewui.com/view-ui-plus/component/form/upload')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//button[@class='ivu-btn ivu-btn-default']").click()
time.sleep(2)
# 输入文件绝对路径
keyboard.send_keys(r"C:\Users\大东\Desktop\tu\black.jpg")
time.sleep(2)
# 键盘上输入"ENTER"
keyboard.send_keys('{ENTER}')
time.sleep(2)