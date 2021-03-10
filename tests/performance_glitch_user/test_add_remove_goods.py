import allure
import pytest
from pytest_testrail.plugin import pytestrail


class TestCountGoods:
    @pytest.mark.fasttest
    @pytestrail.case("C11")
    @allure.story("Проверка добавления/удаления товаров, счетчик корзины")
    @allure.severity("severity")
    def test_count_goods(self, app, login_standart):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Добавить все твоары в корзину
        """
        app.shopping.add_to_cart_buttons_click()
        assert app.shopping.count_goods_text() == 6
        app.shopping.delete_from_cart_buttons_click()
        assert app.shopping.null_count_goods_text() == "Товары удалены"
