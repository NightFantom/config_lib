from typing import Any, Dict


class BaseSource:

    def __init__(self, config: Dict[str, Any]):
        self.__config = config

    def read(self) -> str:
        raise NotImplemented()

    def _get_config(self):
        return self.__config