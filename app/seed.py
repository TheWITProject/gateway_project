from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, name="Zac Efron"),
        User(id=2, name="Rock Lee"),
        User(id=3, name="Casey Leur"),
        User(id=4, name="Jasmine Keen"),
        User(id=5, name="John Smith"),
    ]

    posts = [
        Post(id=1, posts="Hey!", completed=False, user_id=1),
        Post(id=2, posts="Enjoying life", completed=False, user_id=1),
        Post(id=3, posts="Nonstop coding", completed=False, user_id=3),
        Post(id=4, posts="The grind never stops", completed=False, user_id=3),
        Post(id=5, posts="I think my cats hiding from me", completed=False, user_id=2),
        Post(id=6, posts="On my way to Six Flags!!!", completed=False, user_id=2),
        Post(id=7, posts="i love tea more than coffee", completed=False, user_id=5),
        Post(id=8, posts="Learning a new language, brb", completed=False, user_id=3),
        Post(id=9, posts="yup, i love sushi.", completed=False, user_id=2),
        Post(id=10, posts="I am proud of myself!", completed=False, user_id=2),
        Post(id=11, posts="omw to cali", completed=False, user_id=4),
        Post(id=12, posts="i daydream too much lol", completed=False, user_id=4),
        Post(id=13, posts="kinda tired...", completed=False, user_id=1),
        Post(id=14, posts="i should start sleeping earlier ;/", completed=False, user_id=3),
        Post(id=15, posts="i forgot my tweet,, oops", completed=False, user_id=5),
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()