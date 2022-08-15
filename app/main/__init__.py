import os
import logging.config
from flask import Flask
from flask.json import jsonify
from celery import Celery
from .constants import http_status_codes as codes

from .config import config_by_name
from .extensions import (
    db,
    ma,
    migrate,
    jwt,
    cors,
    flask_bcrypt
)

celery = Celery(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    logging.config.dictConfig(config_by_name[config_name].LOGGING)
    
    register_extensions(app)
    register_db(app)
    register_errorhandlers(app)
   
    return app

def register_blueprints(app):
    # app.register_blueprint(todo.todo_bp, url_prefix='/api/v1/todo/')
    # return None
    pass

def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    flask_bcrypt.init_app(app)

    cors.init_app(app, resources={r"/api/*": {"origins": "*"}})

    celery.config_from_object(app.config, force=True)
    celery.conf.update(result_backend=app.config['RESULT_BACKEND'])
    return None

def register_db(app):
    with app.app_context():
        db.create_all()

def register_errorhandlers(app):
    
    @app.errorhandler(codes.HTTP_404_NOT_FOUND)
    def handle_404(exception):
        
        return jsonify({"message": "Item not found"}), codes.HTTP_404_NOT_FOUND

    @app.errorhandler(codes.HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(exception):
        return jsonify({"message": "Something went wrong."}), codes.HTTP_500_INTERNAL_SERVER_ERROR

    @app.route("/favicon.ico")
    def favicon():
        return "", 200
    
    return None
