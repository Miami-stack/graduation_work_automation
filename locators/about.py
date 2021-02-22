from selenium.webdriver.common.by import By


class AboutRedirectLocators:
    ABOUT_REDIRECT = (By.XPATH, '//div[@class="content-container"]')
    ABOUT_PROBLEM_USER = (
        By.XPATH,
        '//h4[@class="title has-text-left has-text-primary"]',
    )
