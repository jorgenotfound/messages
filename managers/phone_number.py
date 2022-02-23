from managers.base import BaseManager


class PhoneNumberManager(BaseManager):
    """
        Class implemented using the DAO patter to connect the DB and perform queries
        related to the phone_number table.
        """

    def search_phone_numbers(self, phone_numbers):
        """
        todo: complete docstrings
        :param phone_numbers: (iterator) list of phone_id
        :return: (list) list of phone_number rows
        """
        # Use a single query to retrieve all the phone numbers to improve performance
        number_query = """
        SELECT phone_number.number
        FROM phone_number
        WHERE phone_id in (%s)
        """
        cursor = self.connection.cursor()
        # Execute the queries with parameters to avoid SQL Injection
        cursor.execute(number_query, (",".join(phone_numbers),))
        numbers_data = cursor.fetchall()
        cursor.close()
        return numbers_data
