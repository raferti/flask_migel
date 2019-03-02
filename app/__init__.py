from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)

# db - объект базы данных
db = SQLAlchemy(app)

# migrate - объект механизма миграции
migrate = Migrate(app, db)

from app import routes, models
