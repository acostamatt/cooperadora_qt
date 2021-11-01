import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
HOST = os.getenv('DB_HOST')
ALIAS = os.getenv('ALIAS')