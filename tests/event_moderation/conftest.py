import pytest
import pandas

from time import sleep
from pathlib import Path

from pages.event_moderation import EventModerationPage
from selenium.webdriver.common.by import By
from core.config.config import Config


@pytest.fixture(scope="function")
def event_moderation_page(driver, config) -> EventModerationPage:
    # ToDo: Refactor this to cookies authorization
    email = driver.find_element(By.XPATH, "//*[@data-testid='email']")
    email.send_keys("wadim.drozd+tests@gmail.com")
    password = driver.find_element(By.XPATH, "//*[@data-testid='password']")
    password.send_keys("sapozogoxa")
    log_me_in_button = driver.find_element(By.XPATH, "//*[@data-testid='submit']")
    log_me_in_button.click()
    sleep(3)

    driver.get(url=config.webdriver.base_url + config.webdriver.moderation_url_path)
    yield EventModerationPage(driver)

def pytest_generate_tests(metafunc):
    if "test_poll_creating" == metafunc.function.__name__:

        test_data = tuple(pandas.read_csv(
            Path(*Config.test_data.event_moderation, f"{metafunc.function.__name__}.csv"), delimiter=","
        ).itertuples(index=False, name=None))

        metafunc.parametrize("question, answer_1, answer_2", test_data)

    if "test_trivia_creating" == metafunc.function.__name__:

        test_data = tuple(pandas.read_csv(
            Path(*Config.test_data.event_moderation, f"{metafunc.function.__name__}.csv"), delimiter=","
        ).itertuples(index=False, name=None))

        metafunc.parametrize("question, points, answer_1, answer_2", test_data)

    if "test_prediction_creating" == metafunc.function.__name__:

        test_data = tuple(pandas.read_csv(
            Path(*Config.test_data.event_moderation, f"{metafunc.function.__name__}.csv"), delimiter=","
        ).itertuples(index=False, name=None))

        metafunc.parametrize("question, answer_1, answer_2, answer_1_points, answer_2_points", test_data)
