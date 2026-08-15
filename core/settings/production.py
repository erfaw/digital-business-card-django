from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]  # TODO (LOW) (PRODUCT) make sure about domain.

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": "database",
        "PORT": "5432",
    }
}
"""Database configurations with Docker service postgres with volume."""

SECRET_KEY = os.environ.get("PRODUCTION_SECRET_KEY")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER_PRODUCTION")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD_PRODUCTION")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
