from selenium.webdriver import Chrome

from pages.authorization.locators_collection import LocatorsCollection
from pages.base.base import BasePage
from pages.events.page import EventsPage
from pages.reset_password.page import ResetPasswordPage

import allure


class AuthorizationPage(BasePage):
    def __init__(self, driver: Chrome) -> None:
        super().__init__(driver)

        self.__locators = LocatorsCollection()

    @property
    def path(self) -> str:
        return "sign-in"

    @property
    def header(self) -> str:
        return self._wait_until_not_visible(self.__locators.header).text

    @property
    def expected_header(self) -> str:
        return "Welcome to\nStreamLayer Studio"

    @allure.step('Opening Reset password page')
    def open_reset_password(self) -> ResetPasswordPage:
        self._wait_until_not_visible(self.__locators.forgot_password_button).click()

        return ResetPasswordPage(self._driver)

    @allure.step('Entering email')
    def enter_email(self, email):
        email_input = self._wait_until_not_visible(self.__locators.email_input)
        email_input.send_keys(f"{email}")

    @allure.step('Entering password')
    def enter_password(self, password):
        email_input = self._wait_until_not_visible(self.__locators.password_input)
        email_input.send_keys(f"{password}")

    @allure.step('Click on the "Log me in" button')
    def click_on_log_me_in_btn(self) -> EventsPage:
        self._wait_until_not_visible(self.__locators.log_me_in_button).click()

        return EventsPage(self._driver)
