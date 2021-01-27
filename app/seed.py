from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="audite.t"),
        User(id=2, username="spongebob.squarepants"),
        User(id=3, username="patrick.star"),
        User(id=4, username="squirward.tentacles"),
        User(id=5, username="mr.krabs"),
    ]

    posts = [
        Post(id=1, users_id=1, content="I Ain't"),
        Post(id=2, users_id=1, content="Never Seen"),
        Post(id=3, users_id=1, content="Two Pretty"),
        Post(id=4, users_id=1, content="Best"),
        Post(id=5, users_id=1, content="Friends"),
        Post(id=6, users_id=2, content="Let's learn about the F.U.N. song!"),
        Post(id=7, users_id=2, content="F is for friends who do stuff together"),
        Post(id=8, users_id=2, content="U is for you and me"),
        Post(id=9, users_id=2, content="N is for anywhere and anytime at all"),
        Post(id=10, users_id=2, content="Down here in the deep blue sea!"),

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()