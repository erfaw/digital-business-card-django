from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = ["*"]  # TODO (LOW) (PRODUCT) make sure about domain.

SECRET_KEY = os.environ.get("LOCAL_SECRET_KEY")
