import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY')

    DEBUG = os.getenv('FLASK_DEBUG', True)
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 15 * 1024 * 1024
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 860597138