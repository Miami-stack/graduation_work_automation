import logging
import time

from common.base import BaseClass
from locators.login import LoginLocators
from locators.main_page import MainLocators

logger = logging.getLogger()


class LoginPage(BaseClass):
    def __init__(self, app):
        self.app = app

    def username_input(self):
        return self.app.driver.find_element(*LoginLocators.USERNAME_INPUT)

    def password_input(self):
        return self.app.driver.find_element(*LoginLocators.PASSWORD_INPUT)

    def login_button(self):
        return self.app.driver.find_element(*LoginLocators.LOGIN_BUTTON)

    def login_button_click(self):
        self.login_button().click()

    def burger_button(self, wait_time=15):
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(*MainLocators.BURGER_BUTTON)
            if len(element) > 0:
                return element[0]
            time.sleep(0.5)
        return 0

    def burger_button_click(self):
        logger.info("Пытаемся нажать кнопку бургер")
        self.burger_button().click()

    def auth(self, username: str, password: str):
        logger.info(
            f"Пытаемся залогиниться с помощью username: {username} и пароля: {password}"
        )
        self.input_value(self.username_input(), username)
        self.input_value(self.password_input(), password)
        self.login_button_click()

    def logout_button(self, wait_time=5):
        logger.info("Пытаемся разлогиниться")
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(*MainLocators.LOGOUT_BUTTON)
            if len(element) > 0:
                return element[0]
            time.sleep(0.5)
        return 0

    def logout_button_click(self):
        self.logout_button().click()

    def items_burger_view(self, wait_time=15):
        logger.info("Пытаемся вытащить итемы с выдвигающегося меню")
        return self.app.driver.find_elements(*MainLocators.BURGER_ITEMS)

    def items(self):
        return [value.text for value in self.items_burger_view()]

    def error_view(self):
        return self.app.driver.find_element(*LoginLocators.ERROR)

    def error_text(self):
        return self.error_view().text
