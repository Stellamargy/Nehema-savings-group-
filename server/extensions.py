from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#create SQLAlchemy and Migrate instances 
db=SQLAlchemy()
migrate=Migrate()