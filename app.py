from flask import Flask, render_template

import datetime
import time

app = Flask(__name__)

# this function calculates how much time has passed since running the program, if the time of running exceeds 2hrs, the timer informs the user to get up and walk, it also returns the "screen time"

def user_timer():
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

# Call the function
user_timer()

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(),noTimeLeft = user_timer())

@app.route('/about/')
def about():
    return render_template('about.html')


