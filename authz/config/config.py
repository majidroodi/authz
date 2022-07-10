from mimetypes import init
from os import environ

class Config:
    ENV = environ.get("TECHLAND_AUTHZ_ENV", "production")
    DEBUG = bool(init(environ.get("TECHLAND_AUTHZ_DEBUG", "0")))
    TESTING = bool(init(environ.get("TECHLAND_AUTHZ_TESTING", "0")))
    SECRET_KEY = environ.get("TECHLAND_AUTHZ_SECRET_KEY", "HARD-HARD-HARD-SECRET-KEY")
