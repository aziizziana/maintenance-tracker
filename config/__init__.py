from os import path, environ
from dotenv import load_dotenv

env_path = path.join(path.dirname(__file__), path.pardir, '.env')
load_dotenv(env_path, override=True)


def get_env(key):
    """
    Get the value to the environment key
    :param key: Environment Key
    :return: String
    """
    return environ.get(key)
