from .base import *

DEBUG = False

# require at least one allowed hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
