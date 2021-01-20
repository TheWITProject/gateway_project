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
        Post(id=1, content="I Ain't"),
        Post(id=2, content="Never Seen"),
        Post(id=3, content="Two Pretty"),
        Post(id=4, content="Best"),
        Post(id=5, content="Friends"),
        Post(id=6, content="Let's learn about the F.U.N. song!"),
        Post(id=7, content="F is for friends who do stuff together"),
        Post(id=8, content="U is for you and me"),
        Post(id=9, content="N is for anywhere and anytime at all"),
        Post(id=10, content="Down here in the deep blue sea!"),

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()