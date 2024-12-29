import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
# driver.get("https://www.baidu.com")
# driver.find_element(By.CSS_SELECTOR, "a[href='http://news.baidu.com']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='http://tieba.baidu.com/']").click()
# time.sleep(4)
# 浏览器的操作
# 刷新浏览器
# driver.refresh()
# 关闭当前窗口
# driver.close()
# 退出浏览器
# driver.quit()


# 窗口最小化
# time.sleep(3)
# driver.minimize_window()


# 获取窗口大小
# size = driver.get_window_size()
# print(size)
# 设置浏览器尺寸
# driver.set_window_size(width=1000, height=1000)

# 获取网页标题
# title = driver.title
# 获取网页url
# url = driver.current_url
# 获取网页源码
# page = driver.page_source
# print(title)
# print(url)
# print(page)

# 网站的前进和后退
# all_handle = driver.window_handles
# driver.switch_to.window(all_handle[1])
# driver.find_element(By.CSS_SELECTOR, "a[href='//help.baidu.com']").click()
# time.sleep(2)
# 回到新闻首页
# driver.back()
# time.sleep(2)
# 回到新闻帮助页面
# driver.forward()




# 浏览器切换窗口
# driver.find_element(By.CSS_SELECTOR, "a[href='http://tieba.baidu.com/']").click()
# driver.find_element(By.CSS_SELECTOR, "a[href='http://news.baidu.com']").click()
# 打印当前句柄
# print(driver.current_window_handle)

# 循环切换线切换第一个窗口，再切换第二个窗口
# for handle in driver.window_handles:
#     driver.switch_to.window(handle)
#     print(driver.current_window_handle)
#     time.sleep(3)

# 判断如果有新的句柄就切换
# current_handle = driver.current_window_handle
# for handle in driver.window_handles:
#     if handle != current_handle:
#         driver.switch_to.window(handle)
#         print(driver.current_window_handle)
#         time.sleep(3)

# 获取当前所有句柄
# all_handle = driver.window_handles
# 通过获取句柄随后用下标切换第个窗口
# driver.switch_to.window(all_handle[1])
# driver.find_element(By.CSS_SELECTOR, "a[href='//help.baidu.com']").click()


# 打开新标签
# driver.switch_to.new_window("tab")
# driver.get("新的网站地址")

# 获取元素的相关信息
# element1 = driver.find_element(By.CSS_SELECTOR, "a[href='http://news.baidu.com']")
# element2 = driver.find_element(By.XPATH, "//span[@class='title-content-title']")
# element3 = driver.find_element(By.ID, 'su')
# time.sleep(4)
# 通过text获取文本信息
# print(element1.text)
# print(element2.text)
# 通过accessible_name获取可用名
# print(element3.accessible_name)

# 获取元素是否可用
driver.get("https://sahitest.com/demo/clicks.htm")
element1 = driver.find_element(By.XPATH, "/html/body/form/input[5]")
element2 = driver.find_element(By.XPATH, "/html/body/form/input[6]")
# 判断元素是否可用
# print(element1.is_enabled())
# print(element2.is_enabled())
# 判断元素是否可选
print(element2.is_selected())
element2.click()
print(element2.is_selected())