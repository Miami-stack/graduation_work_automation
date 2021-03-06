import allure
import pytest
from pytest_testrail.plugin import pytestrail
from common.constants import Users, Burger, Alerts, RandomUserData


class TestAuth:
    @allure.story("Авторизация")
    @allure.severity("blocker")
    @pytestrail.case("C1")
    @pytest.mark.parametrize(
        "username, password",
        (
            (Users.STANDART_USER, Users.PASSWORD),
            (Users.PERFOMANCE_USER, Users.PASSWORD),
        ),
    )
    def test_auth_shop(self, app, username, password):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Кликнуть кнопку "Burger"
        5. Проверить наличие соотвествующих итемов в выдвегающимся меню
        """
        app.open_main_page()
        app.login.auth(username=username, password=password)
        app.login.burger_button_click()
        assert app.login.items() == Burger.ITEMS
        app.login.logout_button_click()

    @allure.story("Авторизация")
    @allure.severity("blocker")
    @pytestrail.case("C1")
    @pytest.mark.xfail(reason="Проблемный юзер сломался")
    def test_auth_shop_for_problem_user(self, app):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Кликнуть кнопку "Burger"
        5. Проверить наличие соотвествующих итемов в выдвегающимся меню
        """
        app.open_main_page()
        app.login.auth(username=Users.PROBLEM_USER, password=Users.PASSWORD)
        app.login.burger_button_click()
        assert app.login.items() == Burger.ITEMS
        app.login.logout_button_click()

    @allure.story("Невалидная авторизация")
    @allure.severity("blocker")
    @pytestrail.case("C2")
    @pytest.mark.parametrize(
        "username, password, alert",
        (
            (Users.INVALID_LOCKED_USER, Users.PASSWORD, Alerts.INVALID_LOCKED_USER),
            (Users.EMPTY_USER, Users.EMPTY_PASSWORD, Alerts.EMPTY_USERNAME),
            ("dsadsaads", Users.EMPTY_PASSWORD, Alerts.EMPTY_PASSWORD),
            (
                RandomUserData.login,
                RandomUserData.password,
                Alerts.INVALID_USERNAME_AND_PASSWORD,
            ),
        ),
    )
    def test_invalid_auth(self, app, username, password, alert):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        """
        app.open_main_page()
        app.login.auth(username=username, password=password)
        assert app.login.error_text() == alert
