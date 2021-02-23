import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from common.logger import setup
from pages.login import LoginPage
from pages.shopping import ShoppingPage
from pages.about import AboutPage
from pages.filter_goods import FilterGoodsPage

logger = logging.getLogger()


class Application:
    def __init__(self, headless, url):
        setup("INFO")
        logger.setLevel("INFO")
        options: Options = Options()
        if headless:
            options.add_argument("--headless")
        self.url = url

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.implicitly_wait(10)
        self.login = LoginPage(self)
        self.shopping = ShoppingPage(self)
        self.about = AboutPage(self)
        self.filter_goods = FilterGoodsPage(self)

    def open_main_page(self):
        logger.info("Open main page")
        self.driver.get(self.url)

    def browser_close(self):
        logger.info("Quit browser")
        self.driver.quit()
