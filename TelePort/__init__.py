from flask import Flask,session
# from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TelePort.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///TelePort.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bpbrpvzttqqlrt:95623fb6a7f594efa00b98589f623d826d4f24eaaf271d5450a99f765f605979@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d5vpcdqgvhjpht'
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
log_manage = LoginManager(app)
from TelePort import routes
