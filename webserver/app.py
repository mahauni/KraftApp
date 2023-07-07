import flask
from flask import Flask
import libs

app = Flask(__name__)


@app.route("/health")
def health():
    return "All healty!!!"


@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello World!</h1>"


@app.route("/esg-image")
def esg():
    libs.esg_image_init()

    img = open("./static/esg.svg", "r")

    return flask.Response(img, mimetype="image/svg+xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
