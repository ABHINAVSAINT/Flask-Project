from flask import Flask, render_template, request, redirect, url_for
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

db = client.MyDatabase

collection = db['Learning']
@app.route('/', methods=['GET', 'POST'])
def home():
    day_of_week = datetime.now().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']

            collection.insert_one({
                "name": name,
                "email": email
            })
            return redirect(url_for('success'))

        except Exception as e:
            return render_template('form.html', error=str(e))
    return render_template('index.html', day=day_of_week, time=current_time)

@app.route('/Register', methods=['POST'])
def register():
    user_data = dict(request.form)
    collection.insert_one(user_data)
    return "Data inserted successfully!"

if __name__ == '__main__':
    app.run(debug=True)