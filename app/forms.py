from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, \
    BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, \
    EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    # Валидатор DataRequired проверяет, что поле не отправлено пустым
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    # Валидатор(validators=) Email() стандартный валидатор Email адреса
    # из wtforms, он проверяет, что в поле формы действительно е-мейл
    email = StringField('email', validators=[DataRequired(), Email()])
    password =PasswordField('Password', validators=[DataRequired()])
    # Валидатор(validators=) EqualTo('password') стандартный валидатор из
    # wtform он проверяет что значение в нем идентично значению поля указанному
    # в аргументах т.е. 'password'
    password2 = PasswordField('Repeat Password',
                              validators=[DataRequired(),
                                          EqualTo('password')]
                              )
    submit = SubmitField('Register')

    # Когда вы добавляете какие-либо методы, соответствующие шаблону
    # validate_<имя_поля>, WTForms принимает их как пользовательские валидаторы
    # и вызывает их в дополнение к стандартным валидаторам.
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')


class EditProfileForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    post = TextAreaField('Say something', validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField('Submit')

