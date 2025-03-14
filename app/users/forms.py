from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_login import current_user
from app.model import User

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=12)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    remember = BooleanField("Remember Me")
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture= FileField('Update profile picture', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()              
            if user:
                raise ValidationError('That username is already taken')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already taken')
            
class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField('Request Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=12)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Request_Password')