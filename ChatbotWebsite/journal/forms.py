from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


# Journal Form
class JournalForm(FlaskForm):
    mood = StringField(
        "How are you feeling?", validators=[DataRequired(), Length(max=30)]
    )
    content = TextAreaField(
        "Express more!", validators=[DataRequired(), Length(max=3000)]
    )
    submit = SubmitField("Submit")
