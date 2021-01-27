from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="Olivia Rodrigo"),
        User(id=2, username="that blonde girl"),
        User(id=3, username="Josh Bassett"),
        User(id=4, username="Drivers License"),
        User(id=5, username="Suhaima Islam"),
    ]

    posts = [
        Post(id=1, content="I got my driver's license last week", user_id=1),
        Post(id=2, content="Just like we always talked about", user_id=1),
        Post(id=3, content="'Cause you were so excited for me", user_id=1),
        Post(id=4, content="To finally drive up to your house", user_id=1),
        Post(id=5, content="But today I drove through the suburbs", user_id=2),
        Post(id=6, content="Crying 'cause you weren't around", user_id=2),
        Post(id=7, content="And you're probably with that blonde girl", user_id=2),
        Post(id=8, content="Who always made me doubt", user_id=3),
        Post(id=9, content="She's so much older than me", user_id=3),
        Post(id=10, content="She's everything I'm insecure about", user_id=3),
        Post(id=11, content="Yeah, today I drove through the suburbs", user_id=4),
        Post(id=12, content="'Cause how could I ever love someone else?", user_id=4),
        Post(id=13, content="And I know we weren't perfect, but I've never felt this way for no one", user_id=4),
        Post(id=14, content="And I know we weren't perfect, but I've never felt this way for no one", user_id=5),
        Post(id=15, content="Guess you didn't mean what you wrote in that song about me", user_id=5),
        Post(id=16, content="'Cause you said forever, now I drive alone past your street", user_id=5),
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()