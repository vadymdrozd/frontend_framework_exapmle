from dataclasses import dataclass

from selenium.webdriver.common.by import By

from core.locator import Locator


@dataclass(frozen=True, init=False)
class LocatorsCollection:
    title: Locator = Locator(By.XPATH, "//*[@data-testid='Events']")