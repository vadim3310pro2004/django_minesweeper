import os
from dotenv import load_dotenv


load_dotenv()

DEBUG = os.environ.get("DEBUG") not in ("False", "false")


if DEBUG:
    from .debug import *
else:
    from .production import *