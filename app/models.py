"""Here you can create your model factory"""


class ModelFactory:
    _client = None
    _database = None

    @staticmethod
    def init_app(uri, database):
        if ModelFactory._client is None:
            # Initialize your client model
            ModelFactory._client = uri
            ModelFactory._database = database

    @staticmethod
    def get_db():
        if ModelFactory._client is None:
            raise Exception('Client not initialized')
        return ModelFactory._client[ModelFactory._database]
