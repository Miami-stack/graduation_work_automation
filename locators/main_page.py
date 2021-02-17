from selenium.webdriver.common.by import By


class MainLocators:
    BURGER_BUTTON = (By.CLASS_NAME, "bm-burger-button")
    BURGER_ITEMS = (By.XPATH, '//nav[@class="bm-item-list"]')
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    GOODS_NAME = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTON = (By.XPATH, '//button[@class="btn_primary btn_inventory"]')
    SHOPPING_CART_BUTTON = (
        By.XPATH,
        "//*[name()='svg']",
    )
