from dataclasses import dataclass

from selenium.webdriver.common.by import By

from core.locator import Locator


@dataclass(frozen=True, init=False)
class LocatorsCollection:
    header: Locator = Locator(By.XPATH, "//*[@class='sc-eLgNKc fQkVwn']")
