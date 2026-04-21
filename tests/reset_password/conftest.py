import pytest

from pages.reset_password import ResetPasswordPage


@pytest.fixture(scope="function")
def reset_password(driver, config) -> ResetPasswordPage:
    driver.get(url=config.webdriver.base_url + config.webdriver.reset_password_url_path)
    yield ResetPasswordPage(driver)
