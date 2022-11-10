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
    academic_record_ref = db.collection('academic_record')
    finance_ref = db.collection('finance')

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

    @app.route('/subjects', methods=['GET'])
    @error_decorator
    def get_subject_by_query_param():
        """"Get subject by query params"""
        args = request.args
        code = args.get('code', default="", type=str)
        component = args.get('component', default="", type=str)
        name = args.get('name', default="", type=str)

        # !TODO: Buscar una forma para no usar tantos condicionales
        if component != "" and name != "" and code != "":
            # Validate all fields
            query = subjects_ref.where(u'code', '==', code).where(u'component', u'==', component).where(u'name', u'==',
                                                                                                        name).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif component == "" and name == "" and code == "":
            # No params/empty params??
            raise SubjectNotFoundException(code)
        elif code != "" and component != "" and name == "":
            # Validate code and component
            query = subjects_ref.where(u'code', '==', code).where(u'component', u'==', component).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif component != "" and name != "" and code == "":
            # Validate component and name
            query = subjects_ref.where(u'component', u'==', component).where(u'name', u'==', name).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif code != "" and name != "" and component == "":
            # Validate code and name
            query = subjects_ref.where(u'code', u'==', code).where(u'name', u'==', name).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif code != "" and component == "" and name == "":
            # Validate only code
            query = subjects_ref.where(u'code', u'==', code).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif component != "" and code == "" and name == "":
            # Validate only component
            query = subjects_ref.where(u'component', u'==', component).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK
        elif name != "" and code == "" and component == "":
            # Validate only name
            query = subjects_ref.where(u'name', u'==', name).stream()
            subject_list = {subject.id: subject.to_dict() for subject in query}
            return jsonify(list(subject_list.values())), HTTPStatus.OK

    @app.route('/subjects/<subject_id>', methods=['GET'])
    @error_decorator
    def get_subject_by_id(subject_id):
        """"Get subject by subject id"""
        subject = subjects_ref.document(subject_id).get()
        if not subject.exists:
            raise SubjectNotFoundException(subject_id)
        return jsonify(subject.to_dict()), HTTPStatus.OK

    @app.route('/subjects/get_all', methods=['GET'])
    @error_decorator
    def get_all_subjects():
        """"Get all subjects"""
        all_subjects = [subject.to_dict() for subject in subjects_ref.stream()]
        return jsonify(all_subjects), HTTPStatus.OK

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

    @app.route('/academic_record', methods=['POST'])
    @error_decorator
    def create_academic_record():
        """"Create academic record"""
        academic_record = academic_record_ref.document(request.json['academicHistoryCode']).get()
        if academic_record.exists:
            raise AcademicRecordAlreadyExistsException(request.json['academicHistoryCode'])
        academic_record_code = request.json['academicHistoryCode']
        academic_record_ref.document(academic_record_code).set(request.json)
        return jsonify({"success": True}), HTTPStatus.CREATED

    @app.route('/academic_record/<academic_record_id>', methods=['GET'])
    @error_decorator
    def get_academic_record_by_id(academic_record_id):
        """"Get academic record by academic record id"""
        academic_record = academic_record_ref.document(academic_record_id).get()
        if not academic_record.exists:
            raise AcademicRecordNotFoundException(academic_record_id)
        return jsonify(academic_record.to_dict()), HTTPStatus.OK

    @app.route('/academic_record/<academic_record_id>', methods=['PUT'])
    @error_decorator
    def update_academic_record_by_id(academic_record_id):
        """"Update academic record by academic record id"""
        academic_record = academic_record_ref.document(academic_record_id).get()
        if not academic_record.exists:
            raise CurriculaNotFoundException(academic_record_id)
        academic_record_code = request.json['academicHistoryCode']
        academic_record_ref.document(academic_record_code).update(request.json)
        return jsonify({"success": True}), HTTPStatus.OK

    @app.route('/finance', methods=['POST'])
    @error_decorator
    def create_receipt():
        """"Create receipt"""
        receipt = finance_ref.document(request.json['student']['studentCode']).get()
        if receipt.exists:
            raise ReceiptAlreadyExistsException(request.json['student']['studentCode'])
        receipt_code = request.json['student']['studentCode']
        finance_ref.document(receipt_code).set(request.json)
        return jsonify({"success": True}), HTTPStatus.CREATED

    @app.route('/finance/<student_receipt_id>', methods=['GET'])
    @error_decorator
    def get_receipt_by_id(student_receipt_id):
        """"Get receipt by receipt id"""
        receipt = finance_ref.document(student_receipt_id).get()
        if not receipt.exists:
            raise ReceiptNotFoundException(student_receipt_id)
        return jsonify(receipt.to_dict()), HTTPStatus.OK

    @app.route('/finance/<student_receipt_id>', methods=['PUT'])
    @error_decorator
    def update_receipt_by_id(student_receipt_id):
        """"Update receipt by receipt id"""
        receipt = finance_ref.document(student_receipt_id).get()
        if not receipt.exists:
            raise ReceiptNotFoundException(student_receipt_id)
        receipt_code = request.json['student']['studentCode']
        finance_ref.document(receipt_code).update(request.json)
        return jsonify({"success": True}), HTTPStatus.OK

    return app
