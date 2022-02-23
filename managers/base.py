from utils.database import DBConnector


class BaseManager:

    def __init__(self, config):
        """
        The connection to the database itself is handled by DBConnector due to separation of concerns,
        this class only contains method to get information using that connection.
        :param config: (Config) Configuration parameters and credentials.
        """
        self.connection = DBConnector(config)

    def __del__(self):
        """
        This will ensure that the connection is closed
        """
        self.connection.close()
