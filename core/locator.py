from typing import Tuple


class Locator:
    def __init__(self, method: str, path: str) -> None:
        self.__method = method
        self.__path = path

    @property
    def tuple(self) -> Tuple[str, str]:
        return self.__method, self.__path
