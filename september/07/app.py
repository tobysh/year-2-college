from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return(render_template("index.html"))

@app.route("/api/")
def api_root():
    return("Hello from the api!")

app.run(port=8000)

