from flask import Flask
from application.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] =0
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from application import routes, models
