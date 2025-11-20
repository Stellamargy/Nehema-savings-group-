from flask import Flask
from .config import Config
from .extensions import db,migrate
#create flask app instance
app=Flask(__name__)

#set configuration in app
app.config.from_object(Config)

#configure db with app
db.init_app(app)
#configure migrate with app and db
migrate.init_app(db=db,app=app)

# Run flask app 
if __name__ == "__main__":
    app.run(debug=True)
