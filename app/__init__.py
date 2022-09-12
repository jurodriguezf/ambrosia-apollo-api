import os

from http import HTTPStatus

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

from app.exceptions.exceptions import SubjectAlreadyExistsException, SubjectNotFoundException


def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Initialize Firestore DB
    template_path = os.path.dirname(__file__) + "/../firebase-key.json"
    cred = credentials.Certificate(template_path)
    default_app = initialize_app(cred)
    db = firestore.client()
    todo_ref = db.collection('todos')

    subjects_ref = db.collection('subjects')
    curricula_ref = db.collection('curricula')

    @app.route('/subjects', methods=['POST'])
    def create_subject():
        try:
            if subjects_ref.document(request.json['code']).get():
                raise SubjectAlreadyExistsException(request.json['code'])
            subject_code = request.json['code']
            subjects_ref.document(subject_code).set(request.json)
            return jsonify({"success": True}), HTTPStatus.CREATED
        except Exception as e:
            return f"An Error Occurred: {e}"

    @app.route('/subjects/<subject_id>', methods=['GET'])
    def get_subject_by_id(subject_id):
        try:
            subject = subjects_ref.document(subject_id).get()
            if subject is None:
                raise SubjectNotFoundException(subject_id)
            return jsonify(subject.to_dict()), 200
        except Exception as e:
            return f"An Error Occurred: {e}"

    @app.route('/list', methods=['GET'])
    def read():
        """
            read() : Fetches documents from Firestore collection as JSON.
            todo : Return document that matches query ID.
            all_todos : Return all documents.
        """
        try:
            # Check if ID was passed to URL query
            todo_id = request.args.get('id')
            if todo_id:
                todo = todo_ref.document(todo_id).get()
                return jsonify(todo.to_dict()), 200
            else:
                all_todos = [doc.to_dict() for doc in todo_ref.stream()]
                return jsonify(all_todos), 200
        except Exception as e:
            return f"An Error Occurred: {e}"

    @app.route('/update', methods=['POST', 'PUT'])
    def update():
        """
            update() : Update document in Firestore collection with request body.
            Ensure you pass a custom ID as part of json body in post request,
            e.g. json={'id': '1', 'title': 'Write a blog post today'}
        """
        try:
            id = request.json['id']
            todo_ref.document(id).update(request.json)
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occurred: {e}"

    @app.route('/delete', methods=['GET', 'DELETE'])
    def delete():
        """
            delete() : Delete a document from Firestore collection.
        """
        try:
            # Check for ID in URL query
            todo_id = request.args.get('id')
            todo_ref.document(todo_id).delete()
            return jsonify({"success": True}), 200
        except Exception as e:
            return f"An Error Occurred: {e}"

    return app
