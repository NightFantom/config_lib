from typing import Any, Dict

class BaseParser:

    def __init__(self, config: Dict[str, Any]):
        self.__config = config

    def parse(self, data: str) -> dict:
        raise NotImplemented
