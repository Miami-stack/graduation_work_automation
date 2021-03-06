import os

import allure
import pytest

from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    url = request.config.getoption("--base-url")
    headless = request.config.getoption("--headless")
    app = Application(headless, url)
    yield app
    app.browser_close()


@pytest.fixture()
def login_standart(request, app):
    login = request.config.getoption("--username_standart")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)
    yield
    app.login.burger_button_click()
    app.login.logout_button_click()


@pytest.fixture()
def login_standart_browser_quit(request, app):
    login = request.config.getoption("--username_standart")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)


@pytest.fixture()
def login_problem(request, app):
    login = request.config.getoption("--username_problem")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)
    yield
    app.login.burger_button_click()
    app.login.logout_button_click()


@pytest.fixture()
def login_problem_browser_quit(request, app):
    login = request.config.getoption("--username_problem")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)


@pytest.fixture()
def login_performance(request, app):
    login = request.config.getoption("--username_performance")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)
    yield
    app.login.burger_button_click()
    app.login.logout_button_click()


@pytest.fixture()
def login_performance_browser_quit(request, app):
    login = request.config.getoption("--username_performance")
    passwd = request.config.getoption("--password")
    app.open_main_page()
    app.login.auth(login, passwd)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        try:
            with open("failures", mode):
                if "app" in item.fixturenames:
                    web_driver = item.funcargs["app"]
                else:
                    print("Fail to take screen-shot")
                    return
            allure.attach(
                web_driver.driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
        except Exception as e:
            print("Fail to take screen-shot: {}".format(e))


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://www.saucedemo.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username_standart",
        action="store",
        default="standard_user",
        help="enter username",
    ),
    parser.addoption(
        "--username_problem",
        action="store",
        default="problem_user",
        help="enter username",
    ),
    parser.addoption(
        "--username_performance",
        action="store",
        default="performance_glitch_user",
        help="enter username",
    )
    parser.addoption(
        "--password",
        action="store",
        default="secret_sauce",
        help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="launching browser without gui",
    )
