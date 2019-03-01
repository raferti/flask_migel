# импортируем переменную app из пакета(папки на верхнем уровне) "app"
from app import app


if __name__ == '__main__':
    app.run(debug=True)