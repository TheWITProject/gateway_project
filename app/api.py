from flask import request, render_template, redirect, jsonify
from app import app, db
from models import User, Post


# @app.route('/', methods=['GET'])
# def get_home():
#     return render_template('index.html')

@app.route('/', methods=['GET'])
def get_home():
    data = Post.query.all()
    all_posts = [item.serialize() for item in data]
    return render_template('index.html', posts=all_posts)
