import os
import time

from flask import render_template, flash, redirect, url_for, request
from app.forms import FeedbackForm
from werkzeug.utils import secure_filename
from app.models import Feedback
from app.utils import allowed_file, get_all_reviews

import sqlite3 as sql


def init_routes(app, db):
    @app.route('/feedback', methods=['GET', "POST"])
    def upload():
        reviews = get_all_reviews()
        if request.method == "POST":
            form = FeedbackForm()

            if form.validate_on_submit():

                user_name = form.username.data
                feedback_text = form.feedback.data
                picture_file = form.picture.data

                if not (picture_file and allowed_file(picture_file.filename)):
                    flash('Отправьте скриншот покупки. Разрешены только файлы .png, .jpg и .jpeg')
                    return redirect('/feedback')

                filename = secure_filename(picture_file.filename)
                picture_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                picture_file.save(picture_path)

                feedback_entry = Feedback(name=user_name, photo=filename, feedback=feedback_text)
                db.session.add(feedback_entry)
                db.session.commit()

                found_feedback = Feedback.query.filter_by(name=user_name, feedback=feedback_text).first()
                if found_feedback:
                    UID = found_feedback.id
                    from bot import send_feedback
                    send_feedback(UID, user_name, picture_path, feedback_text)
                else:
                    print('No matching row found')

                flash('Ваш отзыв отправлен на рассмотрение администраторам!')
                return redirect('/feedback')
            else:
                print(form.errors)
                flash('Проверьте правильность ввода данных')
            return render_template('feedback.html', form=form, reviews=reviews)
        return render_template('feedback.html', reviews=reviews)

    @app.errorhandler(404)
    def not_found(error):
        return redirect('/feedback')
