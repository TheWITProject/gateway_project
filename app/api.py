from flask import request, render_template, redirect
from app import app, db
from models import User, Post

# GET /
@app.route('/', methods=['GET'])
def get_home():
    data = Post.query.all()
    all_posts = [item.serialize() for item in data]
    return render_template('index.html', posts=all_posts)

# GET /users_posts
@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    data = User.query.get(user_id)
    one_user = data.serialize()
    return render_template('user_posts.html', users=[one_user])