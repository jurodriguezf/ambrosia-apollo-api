from http import HTTPStatus

from flask import Blueprint, jsonify

from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

subject_bp = Blueprint("curricula", __name__)


@subject_bp.route("/<curricula:curricula_id>", methods=["GET"])
@error_decorator
def get_subject():
    """"Ping endpoint, for knowing if the app is up"""
    return jsonify(PING_RESPONSE), HTTPStatus.OK
