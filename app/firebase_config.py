import os

import firebase_admin
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, db

load_dotenv()
cred = credentials.Certificate("app/fire_base_conf.json")
firebase_admin.initialize_app(cred, {"databaseURL": os.getenv("databaseURL")})

firestore_db = firestore.client()
realtime_db = db.reference()
