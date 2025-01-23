import os


class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)
    SESSION_TYPE = 'filesystem'
    DEBUG = os.getenv('FLASK_DEBUG', True)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 15 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 860597138
SITE_PATH = 'instance/site.db'
APPROVED_PATH = 'instance/approved.db'
PATH_TO_UPLOADS = "../uploads/"
# TODO: slash in the end of the path to uploads