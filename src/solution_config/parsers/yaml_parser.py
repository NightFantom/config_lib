import yaml

from solution_config.parsers.base_parser import BaseParser


class YAMLParser(BaseParser):

    def parse(self, data: str) -> dict:
        return yaml.load(data)