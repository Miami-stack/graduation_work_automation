import logging
import time

from locators.main_page import MainLocators
from locators.about import AboutRedirectLocators

logger = logging.getLogger()


class AboutPage:
    def __init__(self, app):
        self.app = app

    def about_button(self, wait_time=15):
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(*MainLocators.ABOUT_BUTTON)
            if len(element) > 0:
                return element[0]
            time.sleep(0.5)
        return 0

    def button_click(self):
        logger.info("Кликаем кнопку About")
        self.about_button().click()

    def redirect_view_problem(self, wait_time=15):
        logger.info("Произошел редирект на другую страницу")
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(
                *AboutRedirectLocators.ABOUT_PROBLEM_USER
            )
            if len(element) > 0:
                return element
            time.sleep(0.5)
        return 0

    def redirect_view(self, wait_time=15):
        logger.info("Произошел редирект на другую страницу")
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self.app.driver.find_elements(
                *AboutRedirectLocators.ABOUT_REDIRECT
            )
            if len(element) > 0:
                return element[0]
            time.sleep(0.5)
        return 0

    def redirect_view_text(self):
        return [self.redirect_view().text]

    def redirect_view_problem_text(self, wait_time=15):
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            values = [value.text for value in self.redirect_view_problem()]
            if len(values) > 0:
                return values
            time.sleep(0.5)
        return 0
