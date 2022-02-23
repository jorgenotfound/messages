from abc import ABC, abstractmethod
import boto3
import requests


class MessageHelper:
    """
    Class with a method to send a notification using different channels.
    It uses a configuration value to decide which channel to send the notification and
    the factory pattern to define which class is associated with the selected channel.
    Using the factory pattern we can create new classes to send messages in different ways,
    such as SMS, email, API calls, Push notifications.
    """

    def __init__(self, config):
        self.config = config
        self.available_channels = config.available_channels
        self.notification_services = {
            'SNS': SNSMessageService,
            'API': APIMessageService,
        }

    def send(self, **kwargs):
        """
        Send the message data through multiple channels defined.
        :param kwargs: (dict) the arguments that will be passed to the MessageService subclass.
        """
        for channel in self.available_channels:
            sender = self.notification_services[channel]
            sender(self.config).send(**kwargs)


class MessageService(ABC):
    """
    Abstract class to define how to send a message for a selected channel
    """

    @abstractmethod
    def send(self, **kwargs):
        raise NotImplementedError("You should implement this!")


class SNSMessageService(MessageService):
    """
    Class to send a SMS message with AWS SNS service.
    """

    def __init__(self, config):
        self.client = boto3.client(
            "sns",
            aws_access_key_id=config.aws_access_key_id,
            aws_secret_access_key=config.aws_secret_key,
            region_name=config.aws_region_name,
        )

    def send(self, message, number):
        """
        Send a SMS message using AWS SNS service
        :param message: (str) message to be sent
        :param number: (str) phone number that will receive the message
        """
        self.client.publish(
            PhoneNumber=number,
            Message=message
        )


class APIMessageService(MessageService):
    """
    Class to send a HTTP request sending the message to an api.
    """

    def __init__(self, config):
        self.api_url = config.api_url

    def send(self, message):
        """
        Send a message using a HTTP request
        :param message: (str) message to be sent
        """
        requests.post(
            url=self.api_url,
            data=message,
        )
