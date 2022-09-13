import os

from http import HTTPStatus

from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

from app.decorators import error_decorator
from app.exceptions.exceptions import *


def create_app():
    # Initialize Flask app
    app = Flask(__name__)

    # Initialize Firestore DB
    template_path = os.path.dirname(__file__) + "/../firebase-key.json"
    cred = credentials.Certificate(template_path)
    default_app = initialize_app(cred)
    db = firestore.client()

    subjects_ref = db.collection('subjects')
    curricula_ref = db.collection('curricula')

    @app.route('/subjects', methods=['POST'])
    @error_decorator
    def create_subject():
        """"Create subject"""
        subject = subjects_ref.document(request.json['code']).get()
        if subject.exists:
            raise SubjectAlreadyExistsException(request.json['code'])
        subject_code = request.json['code']
        subjects_ref.document(subject_code).set(request.json)
        return jsonify({"success": True}), HTTPStatus.CREATED

    @app.route('/subjects/<subject_id>', methods=['GET'])
    @error_decorator
    def get_subject_by_id(subject_id):
        """"Get subject by subject id"""
        subject = subjects_ref.document(subject_id).get()
        if not subject.exists:
            raise SubjectNotFoundException(subject_id)
        return jsonify(subject.to_dict()), HTTPStatus.OK

    @app.route('/subjects/<subject_id>', methods=['PUT'])
    @error_decorator
    def update_subject_by_id(subject_id):
        """"Update subject by subject id"""
        subject = subjects_ref.document(subject_id).get()
        if not subject.exists:
            raise SubjectNotFoundException(subject_id)
        subject_code = request.json['code']
        subjects_ref.document(subject_code).update(request.json)
        return jsonify({"success": True}), HTTPStatus.OK

    @app.route('/subjects/curricula', methods=['POST'])
    @error_decorator
    def create_curricula():
        """"Create curricula"""
        curricula = curricula_ref.document(request.json['curricula_info']['code']).get()
        if curricula.exists:
            raise CurriculaAlreadyExistsException(request.json['curricula_info']['code'])
        curricula_code = request.json['curricula_info']['code']
        curricula_ref.document(curricula_code).set(request.json)
        return jsonify({"success": True}), HTTPStatus.CREATED

    @app.route('/subjects/curricula/<curricula_id>', methods=['GET'])
    @error_decorator
    def get_curricula_by_id(curricula_id):
        """"Get curricula by curricula id"""
        curricula = curricula_ref.document(curricula_id).get()
        if not curricula.exists:
            raise CurriculaNotFoundException(curricula_id)
        return jsonify(curricula.to_dict()), HTTPStatus.OK

    @app.route('/subjects/curricula/<curricula_id>', methods=['PUT'])
    @error_decorator
    def update_curricula_by_id(curricula_id):
        """"Update subject by subject id"""
        curricula = curricula_ref.document(curricula_id).get()
        if not curricula.exists:
            raise CurriculaNotFoundException(curricula_id)
        curricula_code = request.json['curricula_info']['code']
        curricula_ref.document(curricula_code).update(request.json)
        return jsonify({"success": True}), HTTPStatus.OK

    return app
