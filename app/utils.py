from config import Config
import sqlite3 as sql

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS


def get_all_reviews():
    conn = sql.connect('instance/approved.db')
    cursor = conn.cursor()
    query = "SELECT * FROM approved_feedbacks LIMIT 50"
    reviews = []
    cursor.execute(query)
    res = cursor.fetchall()
    conn.close()
    for obj in res:
        reviews.append([obj[0], obj[1]])
    return reviews
