from config import get_config
from controllers.message import MessageController
from utils.file_helper import read_file

"""
Get all the configuration parameters and credentials from a configuration class.
This separates all the credentials and sensitive information from the main script 
and makes easier to change the credentials or run the script in different environments.
"""
CONFIG_CLASS = get_config('default')


def process_line(line):
    """
    Read a line data and send messages with its information. It replaces func01
    :param line: (str) the profile and account which will receive the message.
    """
    line_data = line.split(";")
    profile = line_data[1]
    account_type = line_data[0]
    """
    The code to query the information and send the messages was decoupled and moved to a new controller.
    The new controller contains the method to get information and send messages based in a configuration class
    """
    message_controller = MessageController(CONFIG_CLASS)
    message_controller.send_message(profile, account_type)


if __name__ == '__main__':
    """
    The section of the code that actually triggers the execution was wrapped into a __name__ == '__main__' statement,
    this will ensure that the file is read and the messages are sent only when the script is executed but not when the
    module is imported from another module
    """

    """
    the logic to read the file into a new function in a helper module
    """
    lines = read_file("profileDB_id.txt")

    for line in lines:
        process_line(line)
