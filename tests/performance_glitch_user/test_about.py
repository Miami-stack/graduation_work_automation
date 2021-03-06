import allure
from pytest_testrail.plugin import pytestrail
from common.constants import Alerts


class TestAbout:
    @pytestrail.case("C8")
    @allure.story("Проверка About")
    @allure.severity("minor")
    def test_about(self, app, login_performance_browser_quit):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Кликнуть кнопку "Burger"
        5. Кликнуть кнопку About
        6. Проверить произошел ли редирект на другую страницу
        """
        app.login.burger_button_click()
        app.about.button_click()
        assert app.about.redirect_view_text() == Alerts.ABOUT_USER
