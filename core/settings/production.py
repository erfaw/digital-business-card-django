from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False

ALLOWED_HOSTS = ["*"]  # TODO make sure about domain.

SECRET_KEY = os.environ.get("LOCAL_SECRET_KEY")
