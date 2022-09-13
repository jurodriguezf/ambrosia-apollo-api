from functools import wraps
from http import HTTPStatus

from flask import jsonify
from marshmallow import ValidationError

from app.exceptions.exceptions import *
from app.log import logger

ERROR_RESPONSE = "error"


def error_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as ve:
            logger.error(f"{ve.__class__.__name__}: {ve}")
            return (
                jsonify({ERROR_RESPONSE: f"Invalid JSON format ({ve})"}),
                HTTPStatus.BAD_REQUEST,
            )
        except ResourceNotFoundException as rnfe:
            logger.error(f"{rnfe.__class__.__name__}")
            return (
                jsonify({ERROR_RESPONSE: f"{rnfe.resource} with id {rnfe.resource_id} not found"}),
                HTTPStatus.NOT_FOUND,
            )
        except ResourceAlreadyExistsException as raee:
            logger.error(f"{raee.__class__.__name__}")
            return (
                jsonify({ERROR_RESPONSE: f"{raee.resource} with id {raee.resource_id} already exists"}),
                HTTPStatus.CONFLICT,
            )

    return wrapper
