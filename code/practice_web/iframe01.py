import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 通过index进入iframe
# drvier = webdriver.Chrome()
# drvier.maximize_window()
# drvier.get("https://sahitest.com/demo/iframesTest.htm")
# drvier.find_element(By.ID, "checkRecord").clear()
# drvier.find_element(By.ID, "checkRecord").send_keys("666")
# time.sleep(3)
# # 通过index进入iframe内联框架（0开始）
# drvier.switch_to.frame(1)
# # drvier.find_element(By.CSS_SELECTOR, "a[href='linkTest.htm']").click()
# drvier.find_element(By.ID, "open-self").click()
#
# time.sleep(3)
# drvier.close()

# 通过id或者name进入iframe内联框架
# drvier = webdriver.Chrome()
# drvier.maximize_window()
# # 打开本地的html，文件前面要加：file://
# drvier.get("file:///C:/Users/大东/PycharmProjects/pythonProjec/WebAutoTest/HTML/iframe_test.html")
# drvier.find_element(By.ID, "checkRecord").clear()
# drvier.find_element(By.ID, "checkRecord").send_keys("666")
# time.sleep(3)
# # 通过id进入iframe内联框架
# # drvier.switch_to.frame("iframe_id")
# # 通过name进入iframe内联框架
# drvier.switch_to.frame("iframe_name")
# drvier.find_element(By.XPATH, "//span[text()='番剧']").click()
#
# time.sleep(3)
# drvier.close()

# 通过元素定位进入iframe内联框架
# drvier = webdriver.Chrome()
# drvier.maximize_window()
# drvier.get("https://sahitest.com/demo/iframesTest.htm")
# drvier.find_element(By.ID, "checkRecord").clear()
# drvier.find_element(By.ID, "checkRecord").send_keys("666")
# time.sleep(3)
# # 通过css_selector元素父子关系定位内联框赋值给变量
# sle = drvier.find_element(By.CSS_SELECTOR, "body > iframe")
# # switch_to.frame(接收变量)完成进入iframe的操作
# drvier.switch_to.frame(sle)
# drvier.find_element(By.ID, "open-self").click()
#
# time.sleep(3)
# drvier.close()


drvier = webdriver.Chrome()
drvier.maximize_window()
drvier.get("https://sahitest.com/demo/iframesTest.htm")
drvier.find_element(By.ID, "checkRecord").clear()
drvier.find_element(By.ID, "checkRecord").send_keys("666")
time.sleep(3)
sle = drvier.find_element(By.CSS_SELECTOR, "body > iframe")
drvier.switch_to.frame(sle)
# 退出iframe，切换到上一级
# drvier.switch_to.parent_frame()
# 切换到主界面
drvier.switch_to.default_content()
drvier.find_element(By.ID, "checkRecord").clear()
drvier.find_element(By.ID, "checkRecord").send_keys("777")
time.sleep(3)
drvier.close()
