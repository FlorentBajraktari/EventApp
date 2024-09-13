# backend/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)

# backend/run.py
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/api')
app.register_blueprint(event_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
