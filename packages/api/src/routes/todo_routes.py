from __main__ import app
from flask import Flask, request, jsonify

@app.route("/")
def hello():
    return "Hello, World!"