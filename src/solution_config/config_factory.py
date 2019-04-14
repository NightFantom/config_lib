import os
import time
from typing import Any, Dict

from solution_config.parsers.json_parser import JSONParser
from solution_config.parsers.yaml_parser import YAMLParser
from solution_config.sources.datasource import DataSource
from solution_config.sources.file import FileSource
from solution_config.user_config import UserConfig

DATASOURCE_TYPE_KEY = "source_type"
DATASOURCE_PATH_KEY = "path"

NAME_KEY = "name"
USER_CONFIG_KEY = "config"
LAST_UPDATE_KEY = "last_update"
DATASOURCES_KEY = "datasources"
REFRESH_TIME_KEY = "refresh_time"
CONFIGS_KEY = "configs"

SECONDS_IN_MINUTES = 60
NEVER = -1
FILE_EXTENSION_POS = 1


class ConfigFactory:

    def __init__(self, config: Dict[str, Any]):
        self.__config = config
        self.__users_configs = {}

        self.__type_map = {
            "file": FileSource
        }

        self.__parser_map = {
            "json": JSONParser,
            "yml": YAMLParser
        }

        for config_description in self.__config[CONFIGS_KEY]:
            name = config_description[NAME_KEY]
            refresh_time = config_description.get(REFRESH_TIME_KEY, NEVER)
            datasources_description = config_description[DATASOURCES_KEY]
            datasources_list = self.__parse_datasources(datasources_description)
            user_config = UserConfig(name, datasources_list)
            self.__users_configs[name] = {
                USER_CONFIG_KEY: user_config,
                REFRESH_TIME_KEY: refresh_time * SECONDS_IN_MINUTES,
                LAST_UPDATE_KEY: time.time()
            }

    def __parse_datasources(self, datasources_description):
        datasource_list = []
        for datasource_desc in datasources_description:
            source = self.__build_source(datasource_desc)
            parser = self.__build_parser(datasource_desc)
            datasource = DataSource(source, parser)
            datasource.init()
            datasource_list.append(datasource)

        return datasource_list

    def __build_source(self, source_description):
        source_type = source_description[DATASOURCE_TYPE_KEY]
        clazz = self.__type_map[source_type]
        source = clazz(source_description)
        return source

    def __build_parser(self, parser_description):
        path = parser_description[DATASOURCE_PATH_KEY]
        extension_str = os.path.splitext(path)[FILE_EXTENSION_POS]
        extension_str = extension_str[1:]
        clazz = self.__parser_map[extension_str]
        return clazz(parser_description)

    def get_config(self, key):
        config_desc = self.__users_configs[key]
        config = config_desc[USER_CONFIG_KEY]
        refresh_time = config_desc[REFRESH_TIME_KEY]
        if refresh_time != NEVER:
            last_update = config_desc[LAST_UPDATE_KEY]
            current_time = time.time()
            if last_update + refresh_time <= current_time:
                datasources_list = config.get_datasources()
                for ds in datasources_list:
                    ds.init()
        return config
