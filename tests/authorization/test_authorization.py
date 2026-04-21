import allure
import pytest

from core.config.config import Config


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.authorization
def test_url(authorization):
    assert f"{Config().webdriver.base_url}{authorization.path}" == authorization.url

@allure.severity(allure.severity_level.MINOR)
@pytest.mark.authorization
def test_header(authorization):
    """
    In this test we check if everything is okay with header
    """
    assert authorization.expected_header == authorization.header

@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.authorization
def test_authorization(authorization, login, password):
    """
    Test type - positive
    In this test we check if everything is okay with authorization
    """
    authorization.enter_email(login)
    authorization.enter_password(password)
    events_page = authorization.click_on_log_me_in_btn()
    assert "Events" == events_page.title

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.acceptance
@pytest.mark.authorization
def test_reset_password_link(authorization):
    """
    In this test we check if everything is okay with Reset password link
    """
    forgot_password = authorization.open_reset_password()
    assert "Let's find your account\nPlease enter your email" == forgot_password.header
