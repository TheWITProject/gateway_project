from flask import request, render_template, redirect
from app import app, db
from models import User, Post

# GET /
@app.route('/', methods=['GET'])
def get_index():
    data = Post.query.all()
    all_posts = [item.serialize() for item in data]
    return render_template('index.html', posts=all_posts)