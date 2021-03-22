from flask import Flask, render_template
import os
from app import StartDashApp


server = Flask(__name__)

@server.route("/")
def index():
    return render_template("index.html")


@server.route("/about")
def about():
    return render_template("about.html",page_title="About")

@server.route("/dash")
def dashboard():
    pass


if __name__ == "__main__":

    
    StartDashApp(server=server)
    server.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

