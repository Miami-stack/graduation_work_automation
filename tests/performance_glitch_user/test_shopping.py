import allure
import pytest

from common.constants import (
    Goods,
    Order,
    RandomShopData,
    InvalidGoods,
    InvalidCheckoutYourInformation,
)


class TestShopping:
    @allure.story("Покупка товаров")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code",
        (
            (
                RandomShopData.first_name,
                RandomShopData.last_name,
                RandomShopData.postal_code,
            ),
        ),
    )
    def test_shopping(self, app, login_performance, first_name, last_name, postal_code):
        """
        1. Открыть страницу
        2. Выбрать все 6 товаров
        3. Кликнуть корзину
        4. Проверить что выбранные товары добавились
        5. Кликнуть кнопку "Checkout"
        6. Заполнить First Name, Last Name, Zip
        7. Проверить информацию о покупке
        (отображаются нужные товары, отображается соотв. цена)
        8. Кликнуть кнопку FINISH
        """
        app.shopping.buy(data=Goods.ALL_GOODS)
        app.shopping.shopping_cart_button_click()
        assert app.shopping.goods() == Goods.ALL_GOODS
        app.shopping.checkout_button_click()
        app.shopping.input_values(
            first_name=first_name, last_name=last_name, postal_code=postal_code
        )
        assert app.shopping.finish_info_goods_text() == Goods.FINISH_ALL_GOODS
        assert app.shopping.payment_info_text() == Goods.PAYMENT_INFO_ALL_GOODS
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION

    @allure.story("Покупка любых товаров от 1 до 6")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code",
        (
            (
                RandomShopData.first_name,
                RandomShopData.last_name,
                RandomShopData.postal_code,
            ),
        ),
    )
    def test_random_shopping(
        self, app, login_performance, first_name, last_name, postal_code
    ):
        """
        1. Открыть страницу
        2. Выбрать любые товары от 1 до 6
        3. Кликнуть корзину
        4. Проверить что выбранные товары добавились
        5. Кликнуть кнопку "Checkout"
        6. Заполнить First Name, Last Name, Zip
        7. Проверить информацию о покупке
        (отображаются нужные товары, отображается соотв. цена)
        8. Кликнуть кнопку FINISH
        """
        app.shopping.random_buy()
        app.shopping.shopping_cart_button_click()
        app.shopping.checkout_button_click()
        app.shopping.input_values(
            first_name=first_name, last_name=last_name, postal_code=postal_code
        )
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION

    @allure.story("Покупка конкретного товара")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code",
        (
            (
                RandomShopData.first_name,
                RandomShopData.last_name,
                RandomShopData.postal_code,
            ),
        ),
    )
    def test_specific_shopping(
        self, app, login_performance, first_name, last_name, postal_code
    ):
        """
        1. Открыть страницу
        2. Выбрать конкретный товар
        3. Кликнуть корзину
        4. Проверить что выбранные товары добавились
        5. Кликнуть кнопку "Checkout"
        6. Заполнить First Name, Last Name, Zip
        7. Проверить информацию о покупке
        (отображаются нужные товары, отображается соотв. цена)
        8. Кликнуть кнопку FINISH
        """
        app.shopping.specific_buy(name="Sauce Labs Fleece Jacket")
        app.shopping.shopping_cart_button_click()
        app.shopping.checkout_button_click()
        app.shopping.input_values(
            first_name=first_name, last_name=last_name, postal_code=postal_code
        )
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION

    @allure.story("Невалидная покупка без указания товаров")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code",
        (
            (
                RandomShopData.first_name,
                RandomShopData.last_name,
                RandomShopData.postal_code,
            ),
        ),
    )
    def test_invalid_shopping_without_goods(
        self, app, login_performance, first_name, last_name, postal_code
    ):
        """
        1. Открыть страницу
        2. Кликнуть корзину
        3. Кликнуть кнопку "Checkout"
        4. Заполнить First Name, Last Name, Zip
        5. Проверить информацию о покупке
        (отображается соотв. цена == 0)
        6. Кликнуть кнопку FINISH
        """
        app.shopping.shopping_cart_button_click()
        app.shopping.checkout_button_click()
        app.shopping.input_values(
            first_name=first_name, last_name=last_name, postal_code=postal_code
        )
        assert (
            app.shopping.payment_info_text()
            == InvalidGoods.INVALID_PAYMENT_INFO_ALL_GOODS
        )
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION

    @allure.story("Невалидная покупка без указания информации о покупателе")
    @allure.severity("critical")
    @pytest.mark.parametrize(
        "first_name, last_name, postal_code",
        (
            (
                RandomShopData.first_name,
                RandomShopData.last_name,
                RandomShopData.postal_code,
            ),
        ),
    )
    def test_invalid_shopping(
        self, app, login_performance, first_name, last_name, postal_code
    ):
        """
        1. Открыть страницу
        2. Кликнуть корзину
        3. Кликнуть кнопку "Checkout"
        4. Кликнуть "Continue"
        5. После ошибки First Name is required
                    заполнить First Name  нажать Continue
        6. После ошибки  Last Name is required
                    заполнить Last Name  нажать Continue
        7. После ошибки Postal Code is required
                    заполнить Postal Code  нажать Continue
        (отображается соотв. цена == 0)
        8. Проверить информацию о покупке
        (отображаются нужные товары, отображается соотв. цена)
        9. Кликнуть кнопку FINISH
        """
        app.shopping.buy(data=Goods.ALL_GOODS)
        app.shopping.shopping_cart_button_click()
        assert app.shopping.goods() == Goods.ALL_GOODS
        app.shopping.checkout_button_click()
        app.shopping.continue_button_click()
        assert (
            app.shopping.error_text()
            == InvalidCheckoutYourInformation.INVALID_FIRST_NAME
        )
        app.shopping.input_values_firstname(first_name=first_name)
        assert (
            app.shopping.error_text()
            == InvalidCheckoutYourInformation.INVALID_LAST_NAME
        )
        app.shopping.input_values_lastname(last_name=last_name)
        assert (
            app.shopping.error_text()
            == InvalidCheckoutYourInformation.INVALID_POSTAL_CODE
        )
        app.shopping.input_values_postalcode(postal_code=postal_code)
        assert app.shopping.finish_info_goods_text() == Goods.FINISH_ALL_GOODS
        assert app.shopping.payment_info_text() == Goods.PAYMENT_INFO_ALL_GOODS
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION
