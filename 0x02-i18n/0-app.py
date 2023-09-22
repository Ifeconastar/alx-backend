#!/usr/bin/env python3
""" A simple flask app that serves an html page """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """ Home route that serves the
    landing page """

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
