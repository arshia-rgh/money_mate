import firebase_admin

from firebase_admin import credentials, firestore

cred = credentials.Certificate("app/fire_base_conf.json")
firebase_admin.initialize_app(credential=cred)

firestore_db = firestore.client()
