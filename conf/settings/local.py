from .base import *

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": os.getenv("LOCAL_DATABASE_ENGINE"),
        "NAME": os.getenv("LOCAL_DATABASE_NAME"),
        "USER": os.getenv("LOCAL_DATABASE_USER"),
        "PASSWORD": os.getenv("LOCAL_DATABASE_PASSWORD"),
        "HOST": os.getenv("LOCAL_DATABASE_HOST"),
        "PORT": os.getenv("LOCAL_DATABASE_PORT"),
    }
}
