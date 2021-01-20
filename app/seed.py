from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="Zac Efron"),
        User(id=2, username="Rock Lee"),
        User(id=3, username="Casey Leur"),
        User(id=4, username="Jasmine Keen"),
        User(id=5, username="John Smith"),
    ]

    posts = [
        Post(id=1, content="Hey!", user_id=1),
        Post(id=2, content="Enjoying life", user_id=1),
        Post(id=3, content="Nonstop coding", user_id=3),
        Post(id=4, content="The grind never stops", user_id=3),
        Post(id=5, content="I think my cats hiding from me", user_id=2),
        Post(id=6, content="On my way to Six Flags!!!", user_id=2),
        Post(id=7, content="i love tea more than coffee", user_id=5),
        Post(id=8, content="Learning a new language, brb", user_id=3),
        Post(id=9, content="yup, i love sushi.", user_id=2),
        Post(id=10, content="I am proud of myself!", user_id=2),
        Post(id=11, content="omw to cali", user_id=4),
        Post(id=12, content="i daydream too much lol",user_id=4),
        Post(id=13, content="kinda tired...", user_id=1),
        Post(id=14, content="i should start sleeping earlier ;/", user_id=3),
        Post(id=15, content="i forgot my tweet,, oops", user_id=5),
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()