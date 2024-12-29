import os.path
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.get_filepath import download_fild_path

path = download_fild_path() + '下载文件文名'
# 判断文件如果存在就移除
if os.path.exists(path):
    print('文件已存在')
    # 删除已存在的文件
    os.remove(path)
    print('文件已删除')

# 谷歌浏览器的配置
chromeOptions = webdriver.ChromeOptions()
# 下载默认的路径，固定写法
prefs = {"dowmload.default_directory": "{}".format(download_fild_path())}
# 实例化
chromeOptions.add_experimental_option("prefs", prefs)
# 配置到后将chromeOptions放到Chrome里面
driver = webdriver.Chrome(chromeOptions)
driver.maximize_window()

driver.get('https://chromedriver.storage.googleapis.com/index.html')
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "/html/body/table/tbody/tr[154]/td[2]/a").click()

time.sleep(3)
driver.close()
