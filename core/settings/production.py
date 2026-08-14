from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = ["*"]  # TODO (LOW) (PRODUCT) make sure about domain.

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "digital_business_card_django",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "database",
        "PORT": "5432",
    }
}
"""Database configurations with Docker service postgres with volume."""

SECRET_KEY = os.environ.get("PRODUCTION_SECRET_KEY")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER_PRODUCTION")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD_PRODUCTION")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
