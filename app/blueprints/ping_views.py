""""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

ping_bp = Blueprint("ping", __name__)


@ping_bp.route("/", methods=["GET"])
@error_decorator
def ping_pong():
    """"Ping endpoint, for knowing if the app is up"""
    return jsonify(PING_RESPONSE), HTTPStatus.OK
