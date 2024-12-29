import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# execute_script方法，用来执行JavaScript。操作页面元素
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.baidu.com")
# driver.execute_script("document.getElementById('kw').value='selenium'")
# driver.execute_script("document.getElementById('su').click()")
# time.sleep(3)
# driver.close()


# execute_script方法，用来执行JavaScript。操作滚动条
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://news.baidu.com/")
# driver.execute_script("window.scrollTo(0,1000)")
# time.sleep(2)
# # 去到顶部
# driver.execute_script("window.scrollTo(0,0)")
# time.sleep(2)
# # 去到底部
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# time.sleep(3)
# driver.close()

# JS处理元素不可见解决方式，原因有遮罩挡住
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://element.eleme.cn/#/zh-CN/component/form")
# element = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div/div/div[2]/section/div[1]/div[1]/div/form/div[6]/div/div/label[1]/span[2]")
# # 使用argument[0].click()去忽略网页上的遮罩
# driver.execute_script("arguments[0].click();", element)
# time.sleep(3)
# driver.close()


# scrollIntoView将元素定位在可是范围内作进一步操作
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://news.baidu.com/")
element = driver.find_element(By.CSS_SELECTOR, "#tiyu > div.l-left-col.col-mod > ul:nth-child(1) > li.bold-item > a")
driver.execute_script("arguments[0].scrollIntoView();", element)
# 为true，元素的顶端将和其所在滚动区的可视区域的顶端对齐
driver.execute_script("arguments[0].scrollIntoView(True);", element)
# 为false，元素的底端将和其所在滚动区的可视区域的底端对齐
driver.execute_script("arguments[0].scrollIntoView(False);", element)
time.sleep(3)
driver.close()