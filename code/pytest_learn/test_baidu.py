from selenium import webdriver
from selenium.webdriver.common.by import By


def test_baidu():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com/")
    driver.maximize_window()
    title = driver.title
    url = driver.current_url
    text = driver.find_element(By.CSS_SELECTOR, "a[href='http://news.baidu.com']").text
    button_text = driver.find_element(By.ID, "su").accessible_name

    assert title == "百度一下，你就知道"
    assert url == "https://www.baidu.com/"
    assert text == "新闻"
    assert button_text == "百度一下"


