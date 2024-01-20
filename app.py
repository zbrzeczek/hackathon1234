from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

import datetime
import time

app = Flask(__name__)

#<<<<<<< HEAD
# this function calculates how much time has passed since running the program, if the time of running exceeds 2hrs, the timer informs the user to get up and walk, it also returns the "screen time"

def user_sitting_timer():
    noTimeLeft = 0
    while True:
        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Check if 30 seconds have passed
            if elapsed_time >= 7200:
                noTimeLeft = 1
                print("You need to get up and leave your desk immediately, give your eyes some rest")
                break  # Breaks the inner loop to restart the timer


#### function reminding the user to drink water
def user_water_timer():
    noTimeLeft = 0
    while True:
        start_time = time.time()

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            # Check if 30 seconds have passed
            if elapsed_time >= 3600:
                noTimeLeft = 1
                print("You need to drink some water, stay hydrated")
                break  # Breaks the inner loop to restart the timer


#### function reminding the user to look 

#=======
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
#>>>>>>> 2858fbeb298037232f61a9b7a391e2317d2c4386

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(),noTimeLeftforSitting = user_sitting_timer(), drinkWater = user_water_timer())

@app.route('/about/')
def about():
    return render_template('about.html')

#<<<<<<< HEAD

##=======
if (__name__ == "__main__"):
    app.run(debug=True)
    db.create_all()
#>>>>>>> 2858fbeb298037232f61a9b7a391e2317d2c4386
