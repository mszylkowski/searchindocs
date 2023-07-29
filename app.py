from flask import Flask, request, render_template, send_file

from src.utils import setup_dbqa

app = Flask(__name__)

dbqa = None

print("Loaded")

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/query")
def query():
    global dbqa
    query = request.args["q"]
    print(query)
    if dbqa is None:
        dbqa = setup_dbqa()
    response = dbqa({'query': query})
    print(response)
    return render_template("response.html", **response)

@app.route("/data/<path:path>")
def static_file(path):
    return send_file(f"data/{path}")
