# from flask_wtf import Form
# from wtforms.fields import StringField
# from flask_wtf import FlaskForm as Form
# # from wtforms import (StringField, SubmitField)
# # from flask.ext.wtf.html5 import URLField
# from wtforms.validators import DataRequired, url
# from wtforms.widgets.html5 import URLField


from wtforms import Form, BooleanField, StringField, PasswordField, validators

from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField
from wtforms.validators import DataRequired


class BookmarkForm(FlaskForm):
    # description = StringField('Enter the description', validators=[DataRequired()])
    description = StringField('Enter the description',validators=[DataRequired()])
    url = StringField('Enter the URL in http:// format',[validators.Required('Enter URL'),validators.URL('Enter valid url')])
    submit = SubmitField("Send")



class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])




