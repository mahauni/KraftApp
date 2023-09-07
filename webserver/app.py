from flask import Flask
import libs
from flask import Response

app = Flask(__name__)


@app.route("/health")
def health():
    return "All healty!!!"


@app.route("/")
def home():
    return "<h1 style='color:blue'>Hello World!</h1>"


@app.route("/esg.png")
def esg():
    img = libs.esg_image_init()

    return Response(img.getvalue(), mimetype="image/png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
