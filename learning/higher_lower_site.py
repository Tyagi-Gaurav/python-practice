from flask import Flask
import random

app = Flask(__name__)

random_num = random.randint(0, 9)
print(random_num)


@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1> '
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>')


@app.route('/<int:num>')
def guess(num):
    if num > random_num:
        return ('<h1>It\'s too high</h1> '
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>')
    elif num < random_num:
        return ('<h1>It\'s too low</h1> '
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>')
    else:
        return ('<h1>You found the number</h1> '
                '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>')


if __name__ == "__main__":
    app.run(debug=True)
