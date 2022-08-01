from flask import Flask,session
# from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TelePort.db'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
log_manage = LoginManager(app)
from TelePort import routes
