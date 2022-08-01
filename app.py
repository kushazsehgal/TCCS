from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DATA.db'
app.config['SQLALCHEMY_BINDS'] = {
    'manager': 'sqlite:///manager.db',
    'employee': 'sqlite:///employee.db',
    'truck': 'sqlite:///truck.db',
}

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Manager(db.Model):
    __bind_key__ = 'manager'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phoneNumber = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    branchID = db.Column(db.String(80), unique=False, nullable=False)
    passwd = db.Column(db.String(80), unique=False, nullable=False)
    isManager = db.Column(db.Boolean, unique=False, nullable=False)
    def __repr__(self):
        return '<Manager %r>' % self.name

class Truck(db.Model):
    __bind_key__ = 'truck'
    truckID = db.Column(db.String(80), primary_key=True)
    truckType = db.Column(db.String(80), unique=False, nullable=False)
    truckCapacity = db.Column(db.Integer, unique=False, nullable=False)
    truckStatus = db.Column(db.Boolean, unique=False, nullable=False)
    def __repr__(self):
        return '<Truck %r>' % self.truckID

class Employee(db.Model):
    __bind_key__ = 'employee'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    address = db.Column(db.String(120), unique=False, nullable=False)
    phoneNumber = db.Column(db.String(120), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    branchID = db.Column(db.String(80), unique=False, nullable=False)
    passwd = db.Column(db.String(80), unique=False, nullable=False)
    isManager = db.Column(db.Boolean, unique=False, nullable=False)
    def __repr__(self):
        return '<Employee %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

#creae a route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
if __name__ == '__main__':
    app.run(debug=True)