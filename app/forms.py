from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed, FileRequired


class FeedbackForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired()])
    picture = FileField('Upload Image',
                        validators=[
                            FileRequired(),
                            FileAllowed((['jpg', 'png', 'jpeg', 'Images only']))
                        ])
    submit = SubmitField("Upload")

