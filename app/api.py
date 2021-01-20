from flask import request, render_template, redirect
from app import app, db
from models import User, Post

# GET /
@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')