import os
from dotenv import load_dotenv

load_dotenv()

AV_API_KEY = os.getenv("AV_API_KEY", "value does not exist")
AV_API_KEY_2 = os.getenv("AV_API_KEY_2", "value does not exist")