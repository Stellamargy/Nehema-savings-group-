from flask_sqlalchemy import SQLAlchemy
from .base import Base
from flask_migrate import Migrate
db = SQLAlchemy(model_class=Base)
migrate=Migrate()