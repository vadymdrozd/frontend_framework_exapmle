from dataclasses import dataclass

from core.singleton import Singleton


@dataclass(init=False, frozen=True)
class TestDataConfig(Singleton):
    event_moderation = "core", "test_data", "event_moderation"
    authorization = "core", "test_data", "authorization"
