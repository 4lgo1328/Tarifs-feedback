import os
from flask import render_template, flash, redirect, url_for, request
from app.forms import FeedbackForm
from werkzeug.utils import secure_filename
from app.models import Feedback


def init_routes(app, db):
    @app.route('/feedback', methods=['GET', "POST"])
    def upload():
        if request.method == "POST":
            form = FeedbackForm()
            if form.validate_on_submit():
                user_name = form.username.data
                feedback_text = form.feedback.data
                picture_file = form.picture.data

                filename = secure_filename(picture_file.filename)
                picture_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
                picture_file.save(picture_path)
                feedback_entry = Feedback(name=user_name, photo=filename, feedback=feedback_text)
                db.session.add(feedback_entry)
                db.session.commit()
                flash('Ваш отзыв отправлен на рассмотрение администраторам!')
                return redirect(url_for('main'))
            else:
                flash('Проверьте правильность ввода данных')

        return render_template('feedback.html', form=form)

    @app.route('/')
    @app.route('/main/')
    def main():
        return render_template('index.html')
