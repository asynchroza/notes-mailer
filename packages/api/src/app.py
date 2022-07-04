from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
import sys
from json import JSONEncoder
from flask_json_schema import JsonSchema
from bson.json_util import ObjectId

sys.path.insert(1, './routes/')

load_dotenv()

app = Flask(__name__)
schema = JsonSchema(app)

class AppJsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(AppJsonEncoder, self).default(obj)

# IMPORTED ROUTES SHOULD BE BENEATH APP INIT
import todo_routes

app.json_encoder = AppJsonEncoder

cors = CORS(app, resources={r"/list*": {"origins": "*"}})                                                                                                                                                                                                                                                                                                                                                                             

# DO NOT PUSH TO PRODUCTION!
# if __name__ == "__main__":
#     app.run()

