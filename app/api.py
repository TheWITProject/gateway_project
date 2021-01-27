from flask import request, render_template, redirect, jsonify
from app import app, db
from models import User, Post


@app.route('/', methods=['GET'])
def get_home():
    data1 = Post.query.all()
    all_posts = [item.serialize() for item in data1]
    data2= User.query.all()
    all_users = [item.serialize() for item in data2]
    return render_template('index.html', posts=all_posts, users=all_users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    data = User.query.get(user_id)
    one_user = data.serialize()
    return render_template('users.html', users=[one_user])

# @app.route('/posts/query')
# def get_all_posts_by_user():
#     user = request.args.get("user")
#     user_id = User.query.filter(User.username == user).first().id
#     data = Post.query.filter(Post.user_id == user_id).all()
#     all_posts_of_user = [item.serialize() for item in data]
#     return render_template('users.html', user=all_posts_of_user)