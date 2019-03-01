# -*- coding: utf-8 -*-
from app import app
from flask import render_template


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

