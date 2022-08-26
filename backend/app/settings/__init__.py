import contextlib

with contextlib.suppress(ImportError):
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())  # load environment variables from .env when using pycharm

from .apps import *
from .auth import *
from .base import *
from .database import *
from .drf import *
from .languages import *
from .path import *
from .social import *
