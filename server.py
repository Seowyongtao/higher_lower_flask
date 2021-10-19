from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def home_route():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width=200>"


@app.route('/<int:num>')
def compare_num(num):
    random_number = random.randint(0,9)
    number_entered = num
    if random_number > number_entered:
        return f"<h1>Random number is {random_number}, too low, try again !!</h1>"
    elif random_number < number_entered:
        return f"<h1>Random number is {random_number}, too high, try again !!</h1>"
    else:
        return f"<h1>Random number is {random_number}, you found me!!</h1>"


if __name__ == "__main__":
    app.run(debug=True)