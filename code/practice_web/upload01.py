import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.get_filepath import get_black_path

driver = webdriver.Chrome()
driver.maximize_window()
# 获取上传文件路径
path = get_black_path()
driver.get("https://sahitest.com/demo/php/fileUpload.htm")
# 获取input文件上元素
upload = driver.find_element(By.ID, 'file')
# upload.send_keys(r"C:\Users\大东\PycharmProjects\pythonProjec\WebAutoTest\file\black.jpg")# 绝对路径的写法
# 输入上传文件的路径
upload.send_keys(r"{}".format(path))
driver.find_element(By.NAME, "submit").click()
time.sleep(2)
driver.close()

