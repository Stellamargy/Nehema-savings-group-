from flask import Flask

#create flask app instance
app=Flask(__name__)

# Run flask app 
if __name__ == "__main__":
    app.run(debug=True)
