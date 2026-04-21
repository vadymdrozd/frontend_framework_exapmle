from dataclasses import dataclass

from core.singleton import Singleton


@dataclass(init=False, frozen=True)
class WebdriverConfig(Singleton):
    timeout: int = 40
    path: str = "chrome_webdriver:4444"
    base_url: str = "https://studio-13.next.streamlayer.io/"
    moderation_url_path: str = "events/all/id/509/moderation"
    reset_password_url_path: str = "reset-password/email"