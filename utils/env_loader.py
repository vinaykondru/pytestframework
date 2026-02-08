import os
from dotenv import load_dotenv

def load_env_file(env_name):
    """
    Load environment-specific .env file
    Example: .env.qa, .env.dev
    """
    env_path = os.path.join("secrets", f".env.{env_name}")
    load_dotenv(env_path)


def get_secret(key):
    """
    Get secret value from loaded .env
    """
    return os.getenv(key)
