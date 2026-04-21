from selenium.webdriver import Chrome

from pages.base.base import BasePage
from pages.reset_password.locators_collection import LocatorsCollection


class ResetPasswordPage(BasePage):
    def __init__(self, driver: Chrome) -> None:
        super().__init__(driver)

        self.__locators = LocatorsCollection()

    @property
    def path(self) -> str:
        return "reset-password/email"

    @property
    def expected_header(self) -> str:
        return "Let's find your account\nPlease enter your email"

    @property
    def header(self) -> str:
        return self._wait_until_not_visible(self.__locators.header).text
