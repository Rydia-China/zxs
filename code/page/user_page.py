from selenium.webdriver.common.by import By

from base.base_page import BasePage


class UserPage(BasePage):
    # 请登录
    ple_login = (By.CSS_SELECTOR, 'a[href="#/app/login"]')
    # 会员中心
    vip_center = (By.XPATH, '//a[contains(text(),"会员中心")]')
    # 我的订单
    my_order = (By.CSS_SELECTOR, 'a[href="#/app/home/member/order"]')
    # 我的收藏
    my_collect = (By.CSS_SELECTOR, 'a[href="#/app/home/member/collection"]')
    # 我的收货地址
    my_address = (By.CSS_SELECTOR, 'a[href="#/app/home/member/receive"]')
    # 我的购物车
    shopping_cart = (By.CSS_SELECTOR, 'a[href="#/app/shoppingcart/cart"]')




