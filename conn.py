import firebase_admin
from firebase_admin import credentials
from pathlib import Path

JSON_NAME = "tpasenjo-1745d-firebase-adminsdk-gc9yx-3c8b38a6d6.json"
DIRECTORY_PATH = Path(__file__).resolve().parent
JSON_PATH = DIRECTORY_PATH / JSON_NAME

cred = credentials.Certificate(JSON_PATH)
firebase_admin.initialize_app(cred)