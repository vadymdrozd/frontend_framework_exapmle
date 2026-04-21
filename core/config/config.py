from dataclasses import dataclass

from core.config.webdriver_config import WebdriverConfig
from core.config.test_data_config import TestDataConfig
from core.singleton import Singleton


@dataclass(init=False, frozen=True)
class Config(Singleton):
    webdriver: WebdriverConfig = WebdriverConfig()
    test_data: TestDataConfig = TestDataConfig()
