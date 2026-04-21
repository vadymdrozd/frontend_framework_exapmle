from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.config.config import Config
from core.locator import Locator


class BasePage:

    def __new__(cls, *args):
        if not hasattr(cls, "instance"):
            setattr(cls, "instance", super().__new__(cls))

        return getattr(cls, "instance")

    def __init__(self, driver: Chrome) -> None:
        self._driver = driver
        self._config = Config()
        self.__wait = WebDriverWait(
            driver=self._driver,
            timeout=self._config.webdriver.timeout
        )

    @property
    def path(self) -> str:
        raise NotImplemented

    @property
    def url(self) -> str:
        return self._driver.current_url

    def _wait_until_not_visible(self, locator: Locator) -> WebElement:
        return self.__wait.until(
            EC.visibility_of_element_located(locator.tuple)
        )

    def _wait_until_visible(self, locator: Locator):
        self.__wait.until_not(EC.visibility_of_element_located(locator.tuple))
