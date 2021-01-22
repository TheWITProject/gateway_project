from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="abcdefghijklmnopqrstuvwxyzabcd"),
        User(id=2, username="kittykattysammy"),
        User(id=3, username="xammyyyalex"),
        User(id=4, username="olivia_rodrigo_stan"),
        User(id=5, username="joshua_basset_sux"),
        User(id=6, username="blackpink_in_ur_area")
    ]

    posts = [
        Post(id=1, content="i love the alphabet", user_id=1 ),
        Post(id=2, content="wow ur so cool", user_id=2),
        Post(id=3, content="lmao do you think ur edgy", user_id=2),
        Post(id=4, content="RED LIGHTS STOP SIGNS I STILL SEE YOUR FACE IN THE WHITE CARS FRONT YARDS", user_id=4),
        Post(id=5, content="CANT DRIVE PAST THE PLACES WE USED TO GO TO", user_id=5), 
        Post(id=6, content="CAUSE I STILL FUCKING LOVE YOU BABE", user_id=4),
        Post(id=7, content="mona lisa kinda lisa", user_id=6),
        Post(id=8, content="how you like that?", user_id=6),
        Post(id=9, content="did y'all listen to lie lie lie?", user_id=4),
        Post(id=10, content="is supernatural trending on tumblr again?", user_id=3),
        Post(id=11, content="so destiel is canon for the 395th time", user_id=3),
        Post(id=12, content="why are there so many putin destiel posts?", user_id=2),
        Post(id=13, content="i did not need to find out yuri!!!on ice was getting a movie through a spn post", user_id=3),
        Post(id=14, content="wait yuri!!!on ice is getting a movie?", user_id=2),
        Post(id=15, content="there should have been more tea in the new joshua basset song 😔", user_id=1)
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()