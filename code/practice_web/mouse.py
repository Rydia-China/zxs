import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# 鼠标单击演示
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.baidu.com")
# driver.find_element(By.ID, 'kw').send_keys("selenium")
# # 初始化鼠标操作
# action = ActionChains(driver)
# # 找元素
# element = driver.find_element(By.ID, "su")
# # 鼠标单击
# action.click(element).perform()
# time.sleep(3)
# driver.close()

# 鼠标双击演示
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://sahitest.com/demo/clicks.htm")
# # 初始化鼠标操作
# action = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//input[@value='dbl click me']")
# # 鼠标双击
# action.double_click(element).perform()
# time.sleep(3)
# driver.close()

# 鼠标右击演示
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://sahitest.com/demo/clicks.htm")
# # 初始化鼠标操作
# action = ActionChains(driver)
# element = driver.find_element(By.XPATH, "//input[@value='right click me']")
# # 鼠标右击
# action.context_click(element).perform()
# time.sleep(3)
# driver.close()


# 鼠标悬浮
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.baidu.com")
# # 初始化鼠标操作
# action = ActionChains(driver)
# element = driver.find_element(By.CSS_SELECTOR, "a[href='http://www.baidu.com/more/']")
# # 鼠标在百度更多处悬浮
# action.move_to_element(element).perform()
# # 点击百科
# driver.find_element(By.CSS_SELECTOR,"#s-top-more > div:nth-child(3) > a").click()
# time.sleep(3)
# driver.close()


# 鼠标拖放演示
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
# # 初始化鼠标操作
# action = ActionChains(driver)
# 找到开始元素和结束元素
# element_start = driver.find_element(By.ID, "dragger")
# element_end = driver.find_element(By.XPATH, "/html/body/div[4]")
# # 用到drag_and_drop只需传入起始和结束元素
# action.drag_and_drop(element_start, element_end).perform()
# time.sleep(3)
# driver.close()


# 根据坐标点拖动演示
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://iviewui.com/view-ui-plus/component/form/slider")
# 初始化鼠标操作
action = ActionChains(driver)
# 找到起始元素
element = driver.find_element(By.XPATH, "//div[@class='ivu-slider-button']")
# drag_and_drop_by_offset传入（开始元素，X轴像素，Y轴像素）
action.drag_and_drop_by_offset(element, 400, 0).perform()

time.sleep(3)
driver.close()
