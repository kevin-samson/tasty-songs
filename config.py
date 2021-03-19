from dotenv import load_dotenv
from pathlib import Path  # python3 only
import os

# set path to env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """Set Flask configuration vars from .env file."""

    # Load in enviornemnt variables
    TESTING = os.getenv('TESTING')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SERVER = os.getenv('SERVER')
    CLIENT_ID = '44de3ff0881d48c8bf95d687e5c54980'
    CLIENT_SECRET = 'cb44c266456f483bb9efa4b092de9192'
    REDIRECT_URI = 'http://localhost:5000/api_callback'
    SCOPE = 'user-library-read user-read-currently-playing user-read-playback-state'