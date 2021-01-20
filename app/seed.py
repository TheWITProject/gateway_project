from models import User, Post
import datetime

def seed(db):
    users = [
        User(username="abcdefghijklmnopqrstuvwxyzabcd"),
        User(username="kittykattysammy"),
        User(username="xammyyyalex"),
        User(username="olivia_rodrigo_stan"),
        User(username="joshua_basset_sux"),
        User(username="blackpink_in_ur_area")
    ]

    posts = [
        Post(content="i love the alphabet" ),
        Post(content="wow ur so cool"),
        Post(content="lmao do you think ur edgy"),
        Post(content="RED LIGHTS STOP SIGNS I STILL SEE YOUR FACE IN THE WHITE CARS FRONT YARDS"),
        Post(content="CANT DRIVE PAST THE PLACES WE USED TO GO TO"), 
        Post(content="CAUSE I STILL FUCKING LOVE YOU BABE"),
        Post(content="mona lisa kinda lisa"),
        Post(content="how you like that?"),
        Post(content="did y'all listen to lie lie lie?"),
        Post(content="is supernatural trending on tumblr again?"),
        Post(content="so destiel is canon for the 395th time"),
        Post(content="why are there so many putin destiel posts?"),
        Post(content="i did not need to find out yuri!!!on ice was getting a movie through a spn post"),
        Post(content="wait yuri!!!on ice is getting a movie?"),
        Post(content="there should have been more tea in the new joshua basset song 😔")
    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()