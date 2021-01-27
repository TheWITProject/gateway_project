from flask import request, render_template, redirect
from app import app, db
from models import User, Post


# ------------------------------------------------
# TASK ROUTES
# ------------------------------------------------



@app.route('/posts', methods=['GET'])
def all_posts():
    data = Post.query.all()
    all_posts = [item.serialize() for item in data]
    return render_template('index.html', posts=all_posts)