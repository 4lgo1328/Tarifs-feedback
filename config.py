import os


class Config:
    SESSION_PERMANENT = False
    SECRET_KEY = "secret-key"
    SESSION_TYPE = 'filesystem'
    DEBUG = os.getenv('FLASK_DEBUG', True)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 15 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # UPLOAD_FOLDER = 'home/c/cs37164/public_html/uploads' # -- for linux


TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 860597138
SITE_PATH = 'instance/site.db'
APPROVED_PATH = 'instance/approved.db'
PATH_TO_UPLOADS = "http://localhost/uploads/"
# TODO: absolute path in the uploads
# TODO MAKE SYSTEM SAVE FILE IN STATIC DIRECTORY