import config
from config import Config
import sqlite3 as sql


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def get_all_reviews():
    conn = sql.connect(config.APPROVED_PATH)
    cursor = conn.cursor()
    query = "SELECT * FROM approved_feedbacks LIMIT 20"
    reviews = []
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    # TODO: Add absolute path to photo to obj[2] - now it looks like <filename>.<ext>
    for obj in res:
        reviews.append([obj[0], obj[1], config.PATH_TO_UPLOADS + str(obj[2])])
    return reviews[::-1]
