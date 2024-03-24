from flask import Flask

app = Flask(__name__)


@app.route('/')  # Decorator function
def hello_world():
    return "Hello World!"


def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"

    return wrapper_function


def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"

    return wrapper_function


def make_emphasis(function):
    def wrapper_function():
        return f"<em>{function()}</em>"

    return wrapper_function


@app.route('/bye')  # Decorator function
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "Bye!"


@app.route("/user/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
