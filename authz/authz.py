from flask import Flask, Blueprint 
from flask_restful import Api
from authz.config import Config

apiv1_bp = Blueprint("apiv1_bp", __name__, url_defaults="/api/v1")
ap1v1 = Api(apiv1_bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(apiv1_bp)
    return app 