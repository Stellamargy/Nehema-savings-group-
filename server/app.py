from flask import Flask
# from .config import Config
from server.config import Config
# from .models import db ,migrate
from server.models import db , migrate


#create flask app instance
app=Flask(__name__)

#set app's configuration settings from Config
app.config.from_object(Config)

#integrate db with app
db.init_app(app)
#intergrate migrate with app and db
migrate.init_app(db=db,app=app)

# Run flask app 
if __name__ == "__main__":
    app.run(debug=True)
