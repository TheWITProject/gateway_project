from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="olivia_rodrigo"),
        User(id=2, username="that_blonde_girl"),
        User(id=3, username="josh_bassett"),
        User(id=4, username="drivers_license"),
        User(id=5, username="suhaima_islam"),
    ]

    posts = [
        Post(id=1, content="I got my driver's license last week"),
        Post(id=2, content="Just like we always talked about"),
        Post(id=3, content="'Cause you were so excited for me"),
        Post(id=4, content="To finally drive up to your house"),
        Post(id=5, content="But today I drove through the suburbs"),
        Post(id=6, content="Crying 'cause you weren't around"),
        Post(id=7, content="And you're probably with that blonde girl"),
        Post(id=8, content="Who always made me doubt"),
        Post(id=9, content="She's so much older than me"),
        Post(id=10, content="She's everything I'm insecure about"),
        Post(id=11, content="Yeah, today I drove through the suburbs"),
        Post(id=12, content="'Cause how could I ever love someone else?"),
        Post(id=13, content="And I know we weren't perfect, but I've never felt this way for no one"),
        Post(id=14, content="And I know we weren't perfect, but I've never felt this way for no one"),
        Post(id=15, content="Guess you didn't mean what you wrote in that song about me"),
        Post(id=16, content="'Cause you said forever, now I drive alone past your street")
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()