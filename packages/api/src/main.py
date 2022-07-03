import json
import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from flask_cors import CORS
import sys

sys.path.insert(1, './routes/')

load_dotenv()

app = Flask(__name__)
import todo_routes

cors = CORS(app, resources={r"/list*": {"origins": "*"}})                                                                                                                                                                                                                                                                                                                                                                             

mongodb_client = PyMongo(app, uri=os.getenv("MONGO_URI"))
db = mongodb_client.db



if __name__ == "__main__":
    app.debug
    app.run()

