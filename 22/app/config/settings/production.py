from .base import *

DEBUG = False

# require at least one allowed hosts
assert ALLOWED_HOSTS and ALLOWED_HOSTS != ["*"]
