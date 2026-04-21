from dataclasses import dataclass

from selenium.webdriver.common.by import By

from core.locator import Locator


@dataclass(frozen=True, init=False)
class LocatorsCollection:
    header: Locator = Locator(By.XPATH, "//*[@class='sc-fKFxtB inMGpj']")
    email_input: Locator = Locator(By.XPATH, "//*[@data-testid='email']")
    password_input: Locator = Locator(By.XPATH, "//*[@data-testid='password']")
    log_me_in_button: Locator = Locator(By.XPATH, "//*[@data-testid='submit']")
    forgot_password_button: Locator = Locator(By.XPATH, "//*[@data-testid='forgot-password']")
