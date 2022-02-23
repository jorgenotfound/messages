from managers.user import UserManager
from managers.phone_number import PhoneNumberManager
from utils.message_helper import MessageHelper


class MessageController:
    """
    Class with the business logic to get the contact information associated with an user profile
    and send messages to that contact.
    This class can be used in other implementations such as scripts or other controllers to send messages just
    passing the configuration file.
    """

    def __init__(self, config):

        """
        Use a new helper class to manage all the logic related with sending the message
        """
        self.message_sender = MessageHelper(config)
        """
        Replace cnx with a new manager class that contains the logic get information 
        from the DB related to users table and phone_number table
        """
        self.user_manager = UserManager(config)
        self.phone_number_manager = PhoneNumberManager(config)

    def send_message(self, user_profile, account_type):
        """
        New unique function to send messages. It replaces func03, func04, func05 and func06.
        :param user_profile: (str) user profile id.
        :param account_type: (str) account type.
        """
        for (first_name, last_name, phone_number, service_link) in self.get_contact_information(user_profile):
            message = f"Hey {first_name} {last_name} we have some information about your {account_type} account, " \
                      f"please go to {service_link} to get more details."
            self.message_sender.send(message=message, number=phone_number)

    def get_contact_information(self, user_profile):
        """
        Retrieve the contact information associated to a user profile.
        :param user_profile: (str) user profile id.
        :return: (list) list with the contact information associated to the user profile.
        """
        user_profile_data = self.user_manager.get_contact_information(user_profile)
        phone_number_ids = user_profile_data.phone_numbers
        phone_numbers_data = self.phone_number_manager.search_phone_numbers(phone_number_ids)

        contact_information = []
        for number_data in phone_numbers_data:
            contact_information.append(
                (user_profile_data.first_name, user_profile_data.last_name,
                 number_data.phone_number, user_profile_data.service_lint)
            )

        return contact_information
