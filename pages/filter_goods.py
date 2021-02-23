import logging

from selenium.webdriver.support.ui import Select

from locators.main_page import MainLocators

logger = logging.getLogger()


class FilterGoodsPage:
    def __init__(self, app):
        self.app = app

    def filter_goods_dropdown(self):
        return self.app.driver.find_element(*MainLocators.FILTER_DROPDOWN)

    def goods_name(self):
        return self.app.driver.find_elements(*MainLocators.GOODS_NAME)

    def select_filters(self, value):
        select = Select(self.filter_goods_dropdown())
        select.select_by_value(value)

    def goods_name_text(self):
        return [value.text for value in self.goods_name()]
