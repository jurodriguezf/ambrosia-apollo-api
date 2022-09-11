from flask import Flask
# from flask_cors import CORS
# from flask_wtf.csrf import CSRFProtect

from app.blueprints.ping_views import ping_bp
from app.blueprints.subject_views import subject_bp
from app.modules import *

ACTIVE_ENDPOINTS = [
    {"url": "/ping", "bp": ping_bp},
    {"url": "/subjects", "bp": subject_bp},
]


def create_app():
    #template_path = os.path.dirname(__file__) + "/../firebase-key.json"
    # cred = credentials.Certificate(template_path)
    # default_app = initialize_app(cred)
    # db = firestore.client()
    # todo_ref = db.collection('todos')

    app = Flask(__name__)

    # CORS(app)

    # app.config["WTF_CSRF_CHECK_DEFAULT"] = False

    # csrf = CSRFProtect()

    app.url_map.strict_slashes = False

    for endpoint in ACTIVE_ENDPOINTS:
        app.register_blueprint(endpoint.get("bp"), url_prefix=endpoint.get("url"))

    return app
