from os import getenv, path
from dotenv import load_dotenv
from .base import *
from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv("SECRET_KEY")
# "django-insecure-w^8)wc@pc87=c!snwl6amp7)47h437*3t$fya3-ty%!u50&@zn"

# SECURITY WARNING: don't run with debug turned on in prosduction!
DEBUG = getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

ADMIN_URL = getenv("ADMIN_URL")

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"
EMAIL_HOST = getenv("EMAIL_HOST")
EMAIL_PORT = getenv("EMAIL_PORT")
DEFAULT_FROMM_EMAIL = getenv("DEFAULT_FROM_EMAIL")
DOMAIN = getenv("DOMAIN")

MAXIMUM_UPLOAD_SIZE = 1 * 1024 * 1024
