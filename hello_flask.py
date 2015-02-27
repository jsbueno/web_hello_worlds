import flask

app = flask.Flask(__name__)


@app.route("/", defaults={"name": "mundo"})
@app.route("/<name>")
def index(name):
    return "<h1>Alô {}</h1>".format(name)

app.run()