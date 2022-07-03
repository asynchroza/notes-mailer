from copy import copy
from app import app, schema
from flask import Flask, request, jsonify
import os, sys, json
import flask_pymongo
from flask_json_schema import JsonSchema, JsonValidationError

sys.path.insert(1, './models/')
from todo_models import TODO_SCHEMA

client = flask_pymongo.MongoClient(os.getenv("MONGO_URI"))
current_db = client["notes-mailer"]
current_col = current_db["to-dos"]

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]})


@app.route("/api/todo/", methods=['POST']) # data should be sent as raw body
@schema.validate(TODO_SCHEMA)
def add_todo_note():
    data = request.json
    current_col.insert_one(data)
    return jsonify({'success': True, 'message': 'Created ToDo'})

# @app.route("/api/todos/", methods=['POST'])
# def add_todo_note_test():
#     data = request.form
#     return data


# @app.route("/api/todo/<string:id>", methods=['GET'])
# def get_todo_note_by_id(id):
#     return "getting_todo_note"

# @app.route("/api/todos", methods=['GET'])
# def get_todo_notes():
#     return "getting_todo_notes"

# @app.route("/api/todo/<string:id>", methods=['DELETE'])
# def delete_todo_note(id):
#     return "deleting_todo_note"

# @app.route("/api/todo/<string:id>", methods=['PATCH'])
# def patch_todo_note(id):
#     return "patching_todo_note"
