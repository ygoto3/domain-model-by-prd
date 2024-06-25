from dotenv import load_dotenv
load_dotenv()

import os

DATABASE_URL = os.getenv("DATABASE_URL") or 'postgres://postgres@localhost:5432/db'
ALLOWED_ORIGIN = os.getenv("ALLOWED_ORIGIN") or 'http://localhost:8001'
AZURE_OAI_ENDPOINT = os.getenv("AZURE_OAI_ENDPOINT")
AZURE_OAI_KEY = os.getenv("AZURE_OAI_KEY")
AZURE_OAI_DEPLOYMENT = os.getenv("AZURE_OAI_DEPLOYMENT")
AZURE_API_VERSION = os.getenv("AZURE_API_VERSION")
