from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    # Creating a variable
    greeting = "Hello, Flask!"

    # Passing the variable to the template
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)