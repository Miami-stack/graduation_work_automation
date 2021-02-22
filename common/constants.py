from models.shopping_data import ShopData
from models.login import UserData
from models.random_data import RandomData


class Users:
    STANDART_USER = "standard_user"
    PROBLEM_USER = "problem_user"
    INVALID_LOCKED_USER = "locked_out_user"
    PERFOMANCE_USER = "performance_glitch_user"
    EMPTY_USER = ""
    PASSWORD = "secret_sauce"
    EMPTY_PASSWORD = ""


class Burger:
    ITEMS = ["All Items\nAbout\nLogout\nReset App State"]


class Alerts:
    EMPTY_USERNAME = "Epic sadface: Username is required"
    EMPTY_PASSWORD = "Epic sadface: Password is required"
    INVALID_LOCKED_USER = "Epic sadface: Sorry, this user has been locked out."
    INVALID_USERNAME_AND_PASSWORD = (
        "Epic sadface: Username and password do not match any user in this service"
    )
    ABOUT_USER = [
        "CONTINUOUS TESTING CLOUD\nFor the best customer experience, "
        "just add Sauce\nLearn more"
    ]
    ABOUT_PROBLEM_USER = ["We're sorry. We can't find the page you are looking for."]


class Goods:
    ALL_GOODS = [
        "Sauce Labs Backpack",
        "Sauce Labs Bike Light",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Onesie",
        "Test.allTheThings() T-Shirt (Red)",
    ]
    FINISH_ALL_GOODS = [
        "QTYDESCRIPTION\n1\nSauce Labs Backpack\ncarry.allTheThings() "
        "with the sleek, streamlined Sly "
        "Pack that melds uncompromising style with unequaled laptop and tablet "
        "protection.\n$29.99\n1\nSauce Labs Bike "
        "Light\nA red light isn't the desired state in "
        "testing but it sure helps when riding your bike at night."
        " Water-resistant with "
        "3 lighting "
        "modes, 1 AAA battery "
        "included.\n$9.99\n1\nSauce "
        "Labs Bolt T-Shirt\nGet your testing "
        "superhero on with the Sauce Labs bolt T-shirt. From "
        "American Apparel, 100% ringspun combed "
        "cotton, heather gray with red bolt.\n$15.99\n1\nSauce "
        "Labs Fleece Jacket\nIt's not every day "
        "that you come across a midweight quarter-zip fleece "
        "jacket capable of handling everything "
        "from a relaxing day outdoors to a busy day at the office."
        "\n$49.99\n1\nSauce Labs Onesie\nRib "
        "snap infant onesie for the junior automation engineer in deve"
        "lopment. "
        "Reinforced "
        "3-snap "
        "bottom closure, two-needle hemmed sleeved and bottom won't "
        "unravel.\n$7.99\n1\nTest.allTheThings()"
        " T-Shirt (Red)\nThis classic Sauce Labs t-shirt is "
        "perfect to wear when cozying up to "
        "your keyboard to automate a few tests. Super-soft and "
        "comfy ringspun combed cotton.\n$15.99"
    ]

    PAYMENT_INFO_ALL_GOODS = [
        "Payment Information:\nSauceCard "
        "#31337\nShipping Information:\nFREE PONY EXPRESS "
        "DELIVERY!\nItem "
        "total: $129.94\nTax: $10.40\nTotal: $140.34\nCANCEL\nFINISH"
    ]


class Order:
    ORDER_INFORMATION = [
        "THANK YOU FOR YOUR ORDER\nYour order "
        "has been dispatched, and will arrive just as fast as "
        "the pony can get there!"
    ]


class InvalidGoods:
    INVALID_PAYMENT_INFO_ALL_GOODS = [
        "Payment Information:\nSauceCard #31337\nShipping Information:\nFREE PONY "
        "EXPRESS DELIVERY!\nItem total: $0\nTax: $0.00\nTotal: $0.00\nCANCEL\nFINISH"
    ]


class InvalidCheckoutYourInformation:
    INVALID_FIRST_NAME = "Error: First Name is required"
    INVALID_LAST_NAME = "Error: Last Name is required"
    INVALID_POSTAL_CODE = "Error: Postal Code is required"


class RandomGoods:
    data = RandomData.random(Goods.ALL_GOODS)
    RandomGoods = data.randomly


class RandomUserData:
    data = UserData.random()
    login = data.login
    password = data.password


class RandomShopData:
    data = ShopData.random()
    first_name = data.first_name
    last_name = data.last_name
    postal_code = data.postal_code
