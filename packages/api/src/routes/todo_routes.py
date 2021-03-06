from app import app, schema
from flask import request, jsonify
import os, sys
from flask_pymongo import MongoClient
from flask_json_schema import JsonValidationError
from jsonschema import FormatChecker, validate
sys.path.insert(1, './models/')
from todo_models import TODO_SCHEMA_POST, TODO_SCHEMA_PATCH
import json
from bson import objectid

client = MongoClient(os.getenv("MONGO_URI"))
current_db = client["notes-mailer"]
current_col = current_db["to-dos"]

@app.errorhandler(JsonValidationError)
def validation_error(e):
    return jsonify({'error': e.message, 'errors': [validation_error.message for validation_error in e.errors]}), 400


@app.route("/api/todo/", methods=['POST']) # data should be sent as raw body
@schema.validate(TODO_SCHEMA_POST, format_checker=FormatChecker())
def add_todo_note():
    data = request.json
    current_col.insert_one(data)
    return jsonify({'success': True, 'message': 'Created ToDo'})

@app.route("/api/todo/<string:id>", methods=['GET'])
def get_todo_note_by_id(id):
    data = list(current_col.find({'_id':objectid.ObjectId(id)}))
    if data == None:
        return jsonify({'success': False, 'message': 'Document not found'}), 404
    return jsonify(data)

@app.route("/api/todo/", methods=['GET'])
def get_all_todo_notes():
    return jsonify(list(current_col.find({})))

@app.route("/api/todo/<string:id>", methods=['PUT'])
def edit_todo_note(id):
    try:
        data = request.json
        val_response = validate(data, TODO_SCHEMA_PATCH)
    except Exception as e:
        return jsonify({'success': False, 'exception': str(e)})
    

    data = {"$set": data}
    response = current_col.find_one_and_update({"_id": objectid.ObjectId(id)}, data)
    if response is None:
        return jsonify({'success': False, 'message': 'Document not found'}), 400
    return jsonify({'success': True, 'message': 'Document was updated', 'todo': response})

