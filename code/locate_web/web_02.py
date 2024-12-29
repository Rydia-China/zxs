import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
# driver.get("https://www.bilibili.com/")
driver.get("https://www.baidu.com/")
# driver.get("https://element.eleme.cn/#/zh-CN/component/cascader")


# 第一节By.ID元素定位（上）
# element = driver.find_element(By.ID, "kw")
# element.send_keys("selenium")
# element2 = driver.find_element(By.ID, "su")
# element2.click()


# # 第二节By.ID元素定位（上）
# driver.find_element(By.ID, "kw").send_keys("selenium")
# driver.find_element(By.ID, "su").click()


# 第三节By.CSS_NAME元素定位
# driver.find_element(By.CLASS_NAME, "nav-search-input").send_keys("敦煌莫高窟")
# driver.find_element(By.CLASS_NAME, "channel-link").click()

# find_elements是查一组数据，此时可以根据下标去取值
# driver.find_elements(By.CLASS_NAME, "channel-link")[4].click()

# 通过这个方法获取css_name为channel-link的文本信息
# for ele in driver.find_elements(By.CLASS_NAME, "channel-link"):
#     print(ele.text)

# 注意定位的元素中间不能有空格如下
# driver.find_elements(By.CLASS_NAME, "icon-bg icon-bg__channel").click()
# time.sleep(3)

# 第四节根据tag_name定位
# driver.find_element(By.TAG_NAME, "input").send_keys("web自动化测试")
# time.sleep(4)
# driver.close()
# driver.quit()

# 第五节根据By.NAME定位
# driver.find_element(By.NAME, "wd").send_keys("根据name属性定位")

# driver.find_elements(By.NAME, 'wd')[0].send_keys("根据name属性定位")


# 第六节根据LINK_TEXT定位元素,定位可点击的a标签，同样如果存在多个elements通过[下标]取值
# driver.find_element(By.LINK_TEXT, "新闻").click()
# driver.find_elements(By.LINK_TEXT, "新闻")[1].click()


# 第六节下半节，根据PARTIAL_LINK_TEXT定位，模糊匹配包含元素,定位可点击的a标签
# driver.find_element(By.PARTIAL_LINK_TEXT, "新").click()

# 第七节根据CSS_SELECTOR元素定位（上）
# 根据html语言可以知道通过css样式如果是通过id属性之类的需要加#
# driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")
# driver.find_element(By.CSS_SELECTOR, "#su").click()


# 根据html语言可以知道通过css样式如果是根据class属性值之类的需要加.
# driver.find_element(By.CSS_SELECTOR, ".nav-search-input").send_keys("ceshi")


# 百度页面根据name["kw"]、[autocomplete="off"]定位
# driver.find_element(By.CSS_SELECTOR, 'name["kw"]').send_keys("selenium")

# 百度页面根据标签属性定位
# driver.find_element(By.CSS_SELECTOR, "a[href='http://image.baidu.com/']").click()
# # *=模糊匹配-包含image.baidu.com元素
# driver.find_element(By.CSS_SELECTOR, "a[href*='image.baidu.com']").click()
# # 模糊匹配-匹配开头,以什么为开头去匹配
# driver.find_element(By.CSS_SELECTOR, "a[href^='http://image.baidu']").click()
# 模糊匹配-匹配结尾,以什么为结尾
# driver.find_element(By.CSS_SELECTOR, 'a[href$="image.baidu.com/"]').click()
# 组合定位
# driver.find_element(By.CSS_SELECTOR, "input.s_ipt").send_keys("selenium")

# 定位子元素，定位百度新闻#s-top-left是id属性
# driver.find_element(By.CSS_SELECTOR, "div#s-top-left>a").click()
# driver.find_element(By.CSS_SELECTOR, "div.s-top-left-new.s-isindex-wrap>a").click()

# 定位子元素，定位百度图片
# driver.find_element(By.CSS_SELECTOR, "div#s-top-left>a:nth-child(6)").click()
# driver.find_elements(By.CSS_SELECTOR, "div#s-top-left>a")[5].click()
# driver.find_element(By.CSS_SELECTOR, "div#s-top-left>a:first-child").click()

# 第九节XPATH (上)
# 绝对路径
# driver.find_element(By.XPATH, "/html/body/div/div/div[2]/a[3]").click()
# 根据Xpath中id定位
# driver.find_element(By.XPATH, "///input[@id='kw']").send_keys("selenium")
# 根据Xpath中class定位,如果class有多值时全部填写
# driver.find_element(By.XPATH, "///input[@class='s_ipt']").send_keys("selenium")
# 根据Xpath中name定位
# driver.find_element(By.XPATH, "//input[@name='wd']").send_keys("selenium")

# 第十节XPATH (下)
# 多个属性组合定位
# driver.find_element(By.XPATH, "//input[@name='wd' and @class='s_ipt' and @autocomplete='off']").send_keys("selenium")
# 多组数据使用下标定位
# driver.find_element(By.XPATH, "//div[@id ='s-top-left']/a[3]").click()
# 通过子元素找父元素

# 文本等于
# driver.find_element(By.XPATH, "//span[text() ='跟着习近平开启“中国游”']").click()
# 文本包含
# driver.find_element(By.XPATH, "//span[contains(text(),'潘展乐')]").click()
# driver.find_elements(By.XPATH, "//a[contains(text(),'贴吧')]")[1].click()

# 通过同级弟弟元素定位饿了么选框
# driver.find_element(By.XPATH, "//span[text()='默认 click 触发子菜单']/following-sibling::div/div/input").click()

# 通过同级哥哥元素定位
driver.find_element(By.XPATH, "//a[contains(text(),'贴吧') and @class='mnav c-font-normal c-color-t']/preceding-sibling::a[2]").click()

time.sleep(4)
driver.close()
driver.quit()



