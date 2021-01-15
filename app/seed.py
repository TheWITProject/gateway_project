from models import User, Post
import datetime

def seed(db):
    users = [
	User(id=1, username="Bob Smith"),
        User(id=2, username="Shantriya James"),
        User(id=3, username="Alex Alex"),
	User(id=4, username="Mary Mary"),
	User(id=5, username="Bob Bob")

    ]

    posts = [
	Post(id=1, content="Hello world"),
        Post(id=2, content="Life is as sweet as lemons"),
        Post(id=3, content="Love going to the beach"),
        Post(id=4, content="Wish covid was over"),
        Post(id=5, content="ooooh well played December 40th 2020"),
	Post(id=6, content="Has anyone read Lord of the Rings"),
        Post(id=7, content="Who else hates Gwenivere and Lancelot"),
        Post(id=8, content="OOOH did anyone watch season 8 GOT-internet explorer"),
        Post(id=9, content="Software programming is sooo hard"),
        Post(id=10, content="What are databases again????"),
	Post(id=11, content="Did you guys see what they did to Bob the builder?"),
        Post(id=12, content="Someone send me some good songs to listen to"),
        Post(id=13, content="How do you say good morning in Bengali-42 points"),
        Post(id=14, content="Anyone know of some good perfume? I've tried chanel 5 but I think it's a little to primitive for me *flips hair*"),
        Post(id=15, content="Is today Friday the 13th?")
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()
