class UserConfig:

    def __init__(self, name, datasources):
        self.__name = name
        self.__datasources = datasources

    def get_datasources(self):
        return self.__datasources

    def __getitem__(self, item):

        data = None
        for datasource in self.__datasources:
            data = datasource.get_data()
            if data is not None:
                break
        return data[item]