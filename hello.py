from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")  # python decorator
def hello_world():
    return ("<h1>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img src='<img src='https://media.giphy.com/media/uWYjSbkIE2XIMIc7gh/giphy.gif'>")


@app.route("/user/<name>")
def greeting(name):
    return f"Hi there, {name}!"


@app.route("/user/<name>/<int:post_id>")
def show_id(post_id, name):
    return f"Post, {post_id}"


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
