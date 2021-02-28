import logging

from common.base import BaseClass
from locators.main_page import MainLocators
from locators.shopping_cart import ShoppingLocators
from common.constants import RandomGoods

logger = logging.getLogger()


class ShoppingPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def add_to_cart_button(self):
        return self.app.driver.find_element(*MainLocators.ADD_TO_CART_BUTTON)

    def add_to_cart_button_click(self):
        logger.info("Добавление товаров в корзину")
        self.add_to_cart_button().click()

    def shopping_cart_button(self):
        return self.app.driver.find_element(*MainLocators.SHOPPING_CART_BUTTON)

    def shopping_cart_button_click(self):
        self.shopping_cart_button().click()

    def goods_in_shopping_cart(self):
        return self.app.driver.find_elements(*ShoppingLocators.GOODS_ITEMS)

    def goods(self):
        logger.info("Проверяем, что нужные товары содержатся в корзине")
        return [value.text for value in self.goods_in_shopping_cart()]

    def checkout_button(self):
        return self.app.driver.find_element(*ShoppingLocators.CHECKOUT_BUTTON)

    def checkout_button_click(self):
        self.checkout_button().click()

    def first_name_input(self):
        return self.app.driver.find_element(*ShoppingLocators.FIRST_NAME_INPUT)

    def last_name_input(self):
        return self.app.driver.find_element(*ShoppingLocators.LAST_NAME_INPUT)

    def postal_code_input(self):
        return self.app.driver.find_element(*ShoppingLocators.POSTAL_CODE_INPUT)

    def continue_button(self):
        return self.app.driver.find_element(*ShoppingLocators.CONTINUE_BUTTON)

    def input_values(self, first_name, last_name, postal_code):
        logger.info(
            f"Пытаемся заполнить информацию о покупателе\n"
            f" first_name: {first_name} \n"
            f" last_name: {last_name}\n"
            f"postal_code: {postal_code}"
        )
        self.input_value(self.first_name_input(), first_name)
        self.input_value(self.last_name_input(), last_name)
        self.input_value(self.postal_code_input(), postal_code)
        self.continue_button().click()

    def finish_info_goods(self):
        return self.app.driver.find_elements(*ShoppingLocators.FINISH_INFO_GOODS)

    def finish_info_goods_text(self):
        logger.info(
            "Проверяем, что нужные товары содержатся в " "итоговой информации о покупке"
        )
        return [value.text for value in self.finish_info_goods()]

    def payment_info(self):
        return self.app.driver.find_elements(*ShoppingLocators.PAYMENT_INFO)

    def payment_info_text(self):
        logger.info("Проверяем, что отображается корректная цена")
        return [value.text for value in self.payment_info()]

    def finish_button(self):
        return self.app.driver.find_element(*ShoppingLocators.FINISH_BUTTON)

    def finish_button_click(self):
        self.finish_button().click()

    def order_info(self):
        return self.app.driver.find_elements(*ShoppingLocators.ORDER_INFO)

    def order_info_text(self):
        logger.info("Проверяем, что отображается нужная информация после оплаты")
        return [value.text for value in self.order_info()]

    def goods_name(self):
        return self.app.driver.find_elements(*MainLocators.GOODS_NAME)

    def goods_from_main_page(self):
        """Возвращает массив товаров с главной страницы."""
        return [value.text for value in self.goods_name()]

    def buy(self, data: list):
        """Кликает все товары, которые содержатся
        в массиве data."""
        logger.info(f"Покупаем товары: {data}")
        for i in self.goods_from_main_page():
            for j in data:
                if i == j:
                    self.add_to_cart_button_click()

    def random_buy(self):
        logger.info(f"Покупаем товары от 1 до 6: {RandomGoods.RandomGoods}")
        for i in self.goods_from_main_page():
            for j in RandomGoods.RandomGoods:
                if i == j:
                    self.add_to_cart_button_click()

    def specific_buy(self, name):
        logger.info(f"Покупаем один конкретный товар: {name}")
        for i in self.goods_from_main_page():
            if i == name:
                self.add_to_cart_button_click()

    def error_view(self):
        return self.app.driver.find_element(*ShoppingLocators.ERROR)

    def error_text(self):
        return self.error_view().text

    def continue_button_click(self):
        self.continue_button().click()

    def input_values_firstname(self, first_name):
        logger.info(
            f"Пытаемся заполнить в негативном тесте "
            f"информацию о покупателе  first_name: {first_name}\n"
        )
        self.input_value(self.first_name_input(), first_name)
        self.continue_button_click()

    def input_values_lastname(self, last_name):
        logger.info(
            f"Пытаемся заполнить в негативном тесте "
            f"информацию о покупателе last_name: {last_name}\n"
        )
        self.input_value(self.last_name_input(), last_name)
        self.continue_button_click()

    def input_values_postalcode(self, postal_code):
        logger.info(
            f"Пытаемся заполнить в негативном тесте "
            f"информацию о покупателе postal_code: {postal_code}\n"
        )
        self.input_value(self.postal_code_input(), postal_code)
        self.continue_button_click()

    def add_to_cart_buttons(self):
        return self.app.driver.find_elements(*MainLocators.ADD_TO_CART_BUTTON)

    def add_to_cart_buttons_click(self):
        logger.info("Кликаем добавление товаров")
        for value in self.add_to_cart_buttons():
            value.click()

    def counter_goods_view(self):
        return self.app.driver.find_elements(*MainLocators.COUNTER_GOODS_IN_CART)

    def count_goods_text(self):
        for i in self.counter_goods_view():
            if int(i.text) == 6:
                return int(i.text)

    def delete_from_cart_buttons(self):
        return self.app.driver.find_elements(*MainLocators.DELETE_FROM_CART_BUTTON)

    def delete_from_cart_buttons_click(self):
        logger.info("Кликаем удаление товаров из корзины")
        for value in self.delete_from_cart_buttons():
            value.click()

    def null_count_goods_text(self):
        if not self.counter_goods_view():
            return "Товары удалены"
