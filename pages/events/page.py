from selenium.webdriver import Chrome

from pages.events.locators_collection import LocatorsCollection
from pages.base.base import BasePage


class EventsPage(BasePage):
    def __init__(self, driver: Chrome) -> None:
        super().__init__(driver)

        self.__locators = LocatorsCollection()

    @property
    def title(self):
        return self._wait_until_not_visible(self.__locators.title).text
