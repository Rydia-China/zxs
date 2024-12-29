import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os.path
from utils.get_filepath import download_fild_path

driver = webdriver.Chrome()
driver.maximize_window()
# 等待三秒，整个页面加载不完，报超时异常
# driver.set_page_load_timeout(3)
# driver.get("https://www.gogle.com")
# 强制等待
# time.sleep(2)

# 隐型等待:等待3秒钟如果发现元素立刻响应，没找到就报错
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
driver.find_element(By.ID, "kw").send_keys("selenium")
time.sleep(3)
driver.close()


# 显性等待
path = download_fild_path() + '下载文件文名'
# 判断文件如果存在就移除
if os.path.exists(path):
    print('文件已存在')
    os.remove(path)
    print('文件已删除')

# 谷歌浏览器的配置
chromeOptions = webdriver.ChromeOptions()
# 下载默认的文件夹
prefs = {"dowmload.default_directory": "{}".format(download_fild_path())}

chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chromeOptions)
driver.maximize_window()
# 需要实例化
locate = (By.XPATH, "/html/body/table/tbody/tr[154]/td[2]/a")
element = WebDriverWait(driver, 3).until(EC.presence_of_element_located(locate), "找不到元素")
element.click()

driver.get('https://chromedriver.storage.googleapis.com/index.html')

time.sleep(3)
driver.close()


