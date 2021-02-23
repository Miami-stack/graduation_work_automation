import allure
import pytest

from common.constants import (
    Order,
    RandomShopData,
    InvalidGoods,
    InvalidCheckoutYourInformation,
)


class TestShopping:
    @allure.story("Покупка конкретного товара")
    @allure.severity("critical")
    @pytest.mark.skip(reason="Товар после покупки не удаляется")
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
        self, app, login_problem, first_name, last_name, postal_code
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
        app.shopping.specific_buy(name="Sauce Labs Backpack")
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
        self, app, login_problem, first_name, last_name, postal_code
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
    @pytest.mark.skip(reason="Товар после покупки не удаляется")
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
        self, app, login_problem, first_name, last_name, postal_code
    ):
        """
        1. Открыть страницу
        2. Выбрать товары
        3. Кликнуть корзину
        4. Кликнуть кнопку "Checkout"
        5. Кликнуть "Continue"
        6. После ошибки First Name is required
                    заполнить First Name  нажать Continue
        7. После ошибки  Last Name is required
                    заполнить Last Name  нажать Continue
        8. После ошибки Postal Code is required
                    заполнить Postal Code  нажать Continue
        (отображается соотв. цена == 0)
        9. Проверить информацию о покупке
        (отображаются нужные товары, отображается соотв. цена)
        10. Кликнуть кнопку FINISH
        """
        app.shopping.specific_buy(name="Sauce Labs Fleece Jacket")
        app.shopping.shopping_cart_button_click()
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
        app.shopping.finish_button_click()
        assert app.shopping.order_info_text() == Order.ORDER_INFORMATION