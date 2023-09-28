from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")  # python decorator
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run()
