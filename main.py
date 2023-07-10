from flask import Flask, render_template
from api import api
from models import db
import config
from flask_security import Security
from sec import user_datastore


app = Flask(__name__)
app.config.from_object(config)
api.init_app(app)
db.init_app(app)
app.security = Security(app, user_datastore)

@app.get('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)