from managers.base import BaseManager


class UserManager(BaseManager):
    """
    Class implemented using the DAO patter to connect the DB and perform queries
    related to the users table.
    """

    def get_contact_information(self, user_profile):
        """
        # TODO: complete docstrings
        :param user_profile:
        :return:
        """

        user_query = """
        SELECT first_name, last_name, service_link
        FROM users
        WHERE profile = %s
        """
        cursor = self.connection.cursor()
        # Execute the queries with parameters to avoid SQL Injection
        cursor.execute(user_query, (user_profile,))
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
