from selenium.webdriver.common.by import By


class MainLocators:
    BURGER_BUTTON = (By.CLASS_NAME, "bm-burger-button")
    BURGER_ITEMS = (By.XPATH, '//nav[@class="bm-item-list"]')
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    GOODS_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn_primary btn_inventory"]')
    DELETE_FROM_CART_BUTTON = (
        By.XPATH,
        '//button[@class="btn_secondary btn_inventory"]',
    )
    SHOPPING_CART_BUTTON = (
        By.XPATH,
        "//*[name()='svg']",
    )
    ABOUT_BUTTON = (By.XPATH, '//a[@id="about_sidebar_link"]')
    FILTER_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    COUNTER_GOODS_IN_CART = (
        By.XPATH,
        '//span[@class="fa-layers-counter shopping_cart_badge"]',
    )
