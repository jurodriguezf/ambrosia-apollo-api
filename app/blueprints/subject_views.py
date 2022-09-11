from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator

from app.schemas.subject_schema import SubjectSchema

subject_bp = Blueprint("subject", __name__)


@subject_bp.route("/<string:subject_id>", methods=["GET"])
@error_decorator
def get_subject(subject_id: str):
    """"Get subject by id"""
    res = app.subject_controller.get_subject_by_id(subject_id)
    return jsonify(res), HTTPStatus.OK


@subject_bp.route("/", methods=["POST"])
@error_decorator
def post_subject():
    """"Create new subject"""
    subject_req = request.get_json(force=True)

    new_subject = SubjectSchema().load(subject_req)

    res = app.subject_controller.create_subject(new_subject)

    return jsonify(res), HTTPStatus.CREATED
