import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imie = db.Column(db.String(20), unique=False, nullable=False)
    nazwisko = db.Column(db.String(20), unique=False, nullable=False)
    punkty = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.imie}>'

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('about.html')

if (__name__ == "__main__"):
    app.run(debug=True)
    db.create_all()