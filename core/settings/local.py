from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

SECRET_KEY = os.environ.get("LOCAL_SECRET_KEY")

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER_LOCAL")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD_LOCAL")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
