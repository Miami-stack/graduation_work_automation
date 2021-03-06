import allure
import pytest
from common.constants import FilterAlerts
from common.constants import FilterValue
from pytest_testrail.plugin import pytestrail


class TestFilterGoods:
    @pytestrail.case("C14")
    @allure.story("Проверка фильтрации товара")
    @allure.severity("major")
    @pytest.mark.parametrize(
        "value, alert",
        [
            [FilterValue.AZ, FilterAlerts.FILTER_A_Z],
            [FilterValue.ZA, FilterAlerts.FILTER_Z_A],
            [FilterValue.LOHI, FilterAlerts.FILTER_LOW_HIGH],
            [FilterValue.HILO, FilterAlerts.FILTER_HIGH_LOW],
        ],
    )
    def test_filter_goods(self, app, login_performance, value, alert):
        """
        1. Открыть страницу
        2. Заполнить поля username и password валидными данными
        3. Кликнуть кнопку Login
        4. Кликнуть каждый фильтр и провалидировать результаты
        на каждом фильтре
        """

        app.filter_goods.select_filters(value=value)
        assert app.filter_goods.goods_name_text() == alert
