from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")  # python decorator
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/user/<name>")
def greeting(name):
    return f"Hi there, {name}!"


@app.route("/user/<name>/<int:post_id>")
def show_id(post_id, name):
    return f"Post, {post_id}"


@app.route("/bye")
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
