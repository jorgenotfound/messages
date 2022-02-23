import os


class BaseConfig:
    """
    Class to define all the configuation parameters, to avoid security issues
    all credentials will be stored in environment variables.
    You can create a new attribute per each new configuration needed.
    """
    aws_region_name = os.environ.get('AWS_REGION_NAME') or ''
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID') or ''
    aws_secret_key = os.environ.get('AWS_SECRET_KEY') or ''
    db_hostname = os.environ.get('DB_HOSTNAME') or '127.0.0.1'
    db_port = os.environ.get('DB_PORT') or '3306'
    db_username = os.environ.get('DB_USERNAME') or 'myuser'
    db_password = os.environ.get('DB_PASSWORD') or 'mypasword'
    db_name = os.environ.get('DB_NAME') or 'mydb'
    available_channels = ''
    api_url = 'test-api.com/api'


class ProdConfig(BaseConfig):
    available_channels = 'SNS'
    api_url = 'prod-api.com/api'
    pass


get_config = dict(
    default=BaseConfig,
    production=ProdConfig,
)
