import firebase_admin

from firebase_admin import credentials

cred = credentials.Certificate("./fir-test-f61db-firebase-adminsdk-yyuk7-d8ae5261bb.json")
firebase_admin.initialize_app(credential=cred)
