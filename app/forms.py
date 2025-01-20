from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed, FileRequired


class FeedbackForm(FlaskForm):
    username = StringField('Name')
    feedback = TextAreaField('Feedback')
    picture = FileField('Upload Image')

    submit = SubmitField("Upload")


