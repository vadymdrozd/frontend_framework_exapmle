import pytest
import pandas

from pathlib import Path
from pages.authorization import AuthorizationPage
from core.config.config import Config


@pytest.fixture(scope="function")
def authorization(driver) -> AuthorizationPage:
    yield AuthorizationPage(driver)


def pytest_generate_tests(metafunc):
    if "test_authorization" == metafunc.function.__name__:

        test_data = tuple(pandas.read_csv(
            Path(*Config.test_data.authorization, f"{metafunc.function.__name__}.csv"), delimiter=","
        ).itertuples(index=False, name=None))

        metafunc.parametrize("login, password", test_data)