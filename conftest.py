import allure
import pytest

from datetime import datetime

from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

from core.config.config import Config

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome


failed_tests = 0


@pytest.fixture(scope="session")
def config():
    yield Config()


@pytest.fixture(scope="function")
def driver(config):
    options = Options()
    options.add_argument("--headless")
    # driver = Remote(command_executor=config.webdriver.path, options=options)
    service = Service(ChromeDriverManager().install())
    driver = Chrome(service=service, options=options)
    driver.get(url=config.webdriver.base_url)

    yield driver

    driver.quit()


@pytest.fixture(autouse=True)
def make_screenshot(request, driver):
    def _fin():
        global failed_tests

        if request.session.testsfailed > failed_tests:
            test_page = request.node.own_markers[0].name
            failed_test = request.node.name
            failing_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            allure.attach(driver.get_screenshot_as_png(),
                          name=f"{failing_time} {test_page} {failed_test}",
                          attachment_type=allure.attachment_type.PNG)
            failed_tests = request.session.testsfailed

    request.addfinalizer(_fin)

    return _fin
