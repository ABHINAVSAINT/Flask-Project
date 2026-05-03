from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import pymongo as PyMongo
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Configuration
Mongo_URI = os.getenv('MONGO_URI')

client = PyMongo.MongoClient(Mongo_URI)
db = client["todo_db"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        item_name = request.form.get('itemName')
        item_desc = request.form.get('itemDescription')

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_desc
        })

        return "Data submitted successfully"

    except Exception as e:
        return f"Error: {str(e)}"
