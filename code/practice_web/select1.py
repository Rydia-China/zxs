import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# driver.get("https://sahitest.com/demo/selectTest.htm")
driver.get("https://iviewui.com/view-ui-plus/component/form/select")

# 先找到select选框的属性赋值给一个变量
select = Select(driver.find_element(By.ID, "s1"))
# 根据index下标获取，从0开始
select.select_by_index(1)
# 根据option的value进行选择
select.select_by_value("51")
# 根据实际看到的内容进行选择
select.select_by_visible_text("Cell Phone")
time.sleep(3)
driver.close()

# 不是select选框的需要模拟人的操作
driver.find_element(By.XPATH, "//div[@class='ivu-select-selection' and @tabindex='0']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='YMSBdt']/div/div[2]/ul[2]/li[1]").click()
time.sleep(3)
driver.close()