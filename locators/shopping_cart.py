from selenium.webdriver.common.by import By


class ShoppingLocators:
    GOODS_ITEMS = (By.XPATH, '//div[@class="inventory_item_name"]')
    CHECKOUT_BUTTON = (By.XPATH, '//a[@class="btn_action checkout_button"]')
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.XPATH, '//input[@class="btn_primary cart_button"]')
    FINISH_INFO_GOODS = (By.XPATH, '//div[@class="cart_list"]')
    PAYMENT_INFO = (By.XPATH, '//div[@class="summary_info"]')
    FINISH_BUTTON = (By.XPATH, '//a[@class="btn_action cart_button"]')
    ORDER_INFO = (By.ID, "checkout_complete_container")
