from models import User, Post
import datetime

def seed(db):
    users = [
        User(username="olivia_rodrigo")
        User(username="that_blonde_girl")
        User(username="josh_bassett")
        User(username="queen")
        User(username="drivers_license")
    ]

    posts = [
        Post(content="I got my driver's license last week")
        Post(content="Just like we always talked about")
        Post(content="Just like we always talked about")
        Post(content="To finally drive up to your house")
        Post(content="But today I drove through the suburbs")
        Post(content="Crying 'cause you weren't around")
        Post(content="And you're probably with that blonde girl")
        Post(content="Who always made me doubt")
        Post(content="She's so much older than me")
        Post(content="She's everything I'm insecure about")
        Post(content="Yeah, today I drove through the suburbs")
        Post(content="'Cause how could I ever love someone else?")
        Post(content="And I know we weren't perfect, but I've never felt this way for no one")
        Post(content="And I know we weren't perfect, but I've never felt this way for no one")
        Post(content="Guess you didn't mean what you wrote in that song about me")
        Post(content="'Cause you said forever, now I drive alone past your street")
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()