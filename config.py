import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'SECRET_KEY')

    DEBUG = os.getenv('FLASK_DEBUG', True)
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    MAX_CONTENT_LENGTH = 15 * 1024 * 1024
    # Mail server settings (if using Flask-Mail)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
