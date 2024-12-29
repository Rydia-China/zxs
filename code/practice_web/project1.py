import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://sellshop.5istudy.online/sell/user/login_page")

# 输入账号
driver.find_element(By.ID, "username").send_keys("test01")
# 输入密码
driver.find_element(By.ID, "password").send_keys("123456")
# 点击登录
driver.find_element(By.XPATH, "//input[@type='submit' and @value='登录']").click()
# 点击新增
driver.find_element(By.CSS_SELECTOR, "a[href='/sell/seller/product/index']").click()
# 输入名称
driver.find_element(By.NAME, "productName").send_keys("鞠婧祎")
# 输入价格
driver.find_element(By.NAME, "productPrice").send_keys("10000")
# 输入库存
driver.find_element(By.NAME, "productStock").send_keys(1)
# 输入描述
driver.find_element(By.NAME, "productDescription").send_keys("超美丽")
# 输入图片地址
driver.find_element(By.NAME, "productIcon").send_keys("https://p7.itc.cn/images01/20230827/60a51ba1167a4add843e68dd6f6b7bf8.jpeg")
# 选择类别
select = Select(driver.find_element(By.NAME, "categoryType"))
select.select_by_value("33")
# 点击提交
driver.find_element(By.XPATH, "//button[@class = 'btn btn-default' and @type='submit']").click()
time.sleep(3)
driver.close()