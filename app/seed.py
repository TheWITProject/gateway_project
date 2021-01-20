from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username='naimataz'),
        User(id=2, username='samanthap'),
        User(id=3, username='baishaki'),
        User(id=4, username='panchitall'),
        User(id=5, username='auditet')
    ]
    posts = [
        Post(id=1, content='Hello World :)'),
        Post(id=2, content='Do what makes you happy!'),
        Post(id=3, content='Take it one day at a time, because one day is all we got!'),
        Post(id=4, content='You can’t always have a good day, but you can always face a bad day with a good attitude.'),
        Post(id=5, content='When you give up on big ideas you give up on the people whose lives they would have changed.'),
        Post(id=6, content='Remember that wherever your heart is, there you will find your treasure'),
        Post(id=7, content='I hope you have the courage to keep loving deeply in a world that fails to do so.'),
        Post(id=8, content='You already have everything you’ve ever needed within yourself '),
        Post(id=9, content='A smooth sea never made a skilled sailor'),
        Post(id=10, content='Yesterday is history, tomorrow is a mystery, but today is a gift, it is why it’s called the present.'),
        Post(id=11, content='Don’t trade your authenticity for approval.'),
        Post(id=12, content='Strive for progress not for perfection.'),
        Post(id=13, content='Never ever lose that smile it brings so much light.'),
        Post(id=14, content='Unless someone like you cares a whole awful lot, nothing is going to get better. It’s not.'),
        Post(id=15, content='-A loving heart is the truest wisdom'),
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()