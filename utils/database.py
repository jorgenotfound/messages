import mysql.connector


class DBConnector:
    """
    This class will allow to create a connection to the database,
    this connector can be used not only in the base script but also in other
    modules where is needed to connect to the database.
    """

    def __init__(self, config):
        self.connection = mysql.connector.connect(
            user=config.db_username,
            password=config.db_password,
            host=config.db_hostname,
            port=config.db_port,
            database=config.db_name,
        )

    def cursor(self):
        """
        Returns the cursor to perform queries within the database
        :return: (Cursor) Cursor instance.
        """
        return self.connection.cursor()

    def close(self):
        """
        Close the connection with the DB.
        """
        self.connection.close()
