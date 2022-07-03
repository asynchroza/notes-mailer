import json
import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
import sys
from flask_json_schema import JsonSchema

sys.path.insert(1, './routes/')

load_dotenv()

app = Flask(__name__)
schema = JsonSchema(app)
import todo_routes

cors = CORS(app, resources={r"/list*": {"origins": "*"}})                                                                                                                                                                                                                                                                                                                                                                             


# DO NOT PUSH TO PRODUCTION!
if __name__ == "__main__":
    app.run()

