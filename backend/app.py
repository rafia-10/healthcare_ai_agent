from flask import Flask, render_template, request, jsonify
from models import init_db
from workflow_service import handle_user_input
import os

template_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'frontend', 'templates')
app = Flask(__name__, template_folder=template_dir)


init_db()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_input():
    user_input = request.json.get("user_input")
    response_text = handle_user_input(user_input)
    return render_template("index.html", response=response_text)