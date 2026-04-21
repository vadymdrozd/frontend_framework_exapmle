import pytest
import allure

from core.config.config import Config


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.reset_password
def test_url(reset_password):
    assert f"{Config().webdriver.base_url}{reset_password.path}" == reset_password.url

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.reset_password
def test_header(reset_password):
    assert reset_password.expected_header == reset_password.header
