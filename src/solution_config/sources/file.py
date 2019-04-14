import os

from solution_config.sources.base_source import BaseSource


class FileSource(BaseSource):

    def read(self):
        config = self._get_config()
        path = config["path"]

        is_optional = config.get("optional", False)
        path_exist = os.path.exists(path)
        data = None
        if not is_optional or path_exist:
            with open(path, mode="r") as file:
                data = file.read()

        return data