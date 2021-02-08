from selenium.webdriver.remote.webelement import WebElement


class BaseClass:
    def input_value(self, element: WebElement, text: str):
        """
        Проверка на то, что заполняем поля не типом None
        """
        if text is not None:
            element.send_keys(text)
