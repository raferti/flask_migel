# -*- coding: utf-8 -*-
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


# Декоратор изменяет функцию, которая следует за ней.
# связываем URL-адреса / и /index с функцией index
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'vovan'}
    posts = [
        {
            'author': {'username': 'Привет'},
            'body': 'Very good'
        },
        {
            'author': {'username': 'Dima'},
            'body': 'Very bad'
        }
    ]

    # Jinja2 заменяет блоки {{...}} соответствующими значениями,
    # заданными аргументами, указанными в вызове render_template()
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    # validate_on_submit() выполняет всю обработку формы
    # Когда отправляется POST запрос при нажатии кнопки submit,
    # validate_on_submit() собирает все данные, запускает все валидаторы,
    # прикрепленные к полям, и если все в порядке, вернет True,
    # сообща что данные действительны и могут быть обработаны приложением.
    # Но если хотя бы одно поле не подтвердит проверку, функция вернет False,
    # и это приведет к тому, что форма будет возвращена пользователю,
    # например, в случае запроса GET.
    if form.validate_on_submit():
        # flash() — полезный способ показать сообщение пользователю.
        # при вызове flash(), Flask сохраняет сообщение, но
        # для показа сообщений необходимо еще доработать шаблон
        flash('Login requested for user {} remember_me{} '.format(
            form.username.data, form.remember_me.data))
        return redirect('index')
    return render_template('login.html', title='Sign in', form=form)

