from firebase_admin import credentials, initialize_app, firestore

import os

from app.controllers.subject_controller import SubjectController


def db_session():
    # Initialize Firestore DB
    template_path = os.path.dirname(__file__) + "/../firebase-key.json"
    cred = credentials.Certificate(template_path)
    default_app = initialize_app(cred)
    db = firestore.client()

    return db


db = db_session()

subject_controller = SubjectController(db_session=db)
