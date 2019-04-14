from typing import Any, Dict

from solution_config.parsers.base_parser import BaseParser
from solution_config.sources.base_source import BaseSource


class DataSource:

    def __init__(self, source: BaseSource, parser: BaseParser):
        self.__source = source
        self.__parser = parser
        self.__data = None

    def init(self):
        self.__data = None
        raw_data = self.__source.read()
        if raw_data is not None:
            self.__data = self.__parser.parse(raw_data)


    def get_data(self) -> Dict[str, Any]:
        return self.__data
