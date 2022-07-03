from app import app, schema
from flask import request, jsonify
import os, sys
from flask_pymongo import MongoClient
from flask_json_schema import JsonValidationError
from jsonschema import FormatChecker, validate
sys.path.insert(1, './models/')
from todo_models import TODO_SCHEMA_POST

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
    data = current_col.find_one({"id":id})
    if data == None:
        return jsonify({'success': False, 'message': 'Document not found'}), 404
    return data 

