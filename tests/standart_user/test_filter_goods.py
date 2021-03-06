import allure
import pytest
from pytest_testrail.plugin import pytestrail

from common.constants import FilterAlerts
from common.constants import FilterValue


class TestFilterGoods:
    @allure.story("Проверка фильтрации товара")
    @allure.severity("major")
    @pytestrail.case("C12")
    @pytest.mark.parametrize(
        "value, alert",
        [
            [FilterValue.AZ, FilterAlerts.FILTER_A_Z],
            [FilterValue.ZA, FilterAlerts.FILTER_Z_A],
            [FilterValue.LOHI, FilterAlerts.FILTER_LOW_HIGH],
            [FilterValue.HILO, FilterAlerts.FILTER_HIGH_LOW],
        ],
    )
    def test_filter_goods(self, app, login_standart, value, alert):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Кликнуть каждый фильтр и провалидировать результаты
        на каждом фильтре
        """

        app.filter_goods.select_filters(value=value)
        assert app.filter_goods.goods_name_text() == alert
