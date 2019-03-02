# импортируем переменную app из пакета(папки на верхнем уровне) "app"
from app import app, db
from app.models import User, Post


if __name__ == '__main__':
    app.run(debug=True)


# Декоратор app.shell_context_processor регистрирует функцию
# как функцию контекста оболочки. Когда запускается команда flask shell,
# она будет вызывать эту функцию и регистрировать элементы,
# возвращаемые ею в сеансе оболочки.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}