import json

from solution_config.parsers.base_parser import BaseParser


class JSONParser(BaseParser):

    def parse(self, data: str) -> dict:
        return json.loads(data)
