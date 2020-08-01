import flask
import db

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    l = db.getAllBudget()
    print(l)
    l = list(zip(*l))
    print(l)
    return "<h>Yeah it works.</h>"

app.run()