from flask_migrate import Migrate


db = SQLAlchemy(model_class=Base)


migrate=Migrate()