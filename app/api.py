from flask import request, render_template, redirect
from app import app, db
from models import User, Post


@app.route('/', methods=['GET'])
def all_posts():
    data = Post.query.all()
    posts_all = [item.serialize() for item in data]
    return render_template('index.html', posts = posts_all)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    data = User.query.get(user_id)
    one_user = data.serialize()
    return render_template('users.html', users = [one_user])