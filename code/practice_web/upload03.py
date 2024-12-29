import time
from pywinauto import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//*[@id='form']/span[1]/span[1]").click()
time.sleep(3)
driver.find_element(By.XPATH, "//*[@id='form']/div/div[2]/div[2]/input").click()
time.sleep(2)
# 输入文件绝对路径
keyboard.send_keys(r"C:\Users\大东\PycharmProjects\pythonProjec\WebAutoTest\file\img.png")
time.sleep(2)
keyboard.send_keys('{ENTER}')
time.sleep(2)