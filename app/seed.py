from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="bilbolivia"),
        User(id=2, username="baishakicodes"),
        User(id=3, username="panchitalopez"),
        User(id=4, username="auditetalukder"),
        User(id=5, username="naimataz")
    ]

    posts = [
        Post(id=1, content="Just wrapped up a cereal fight with my mom and dad. What a night.", user_id=1),
        Post(id=3, content="Captain Olivia Benson off duty like -", user_id=3),
        Post(id=4, content="Can you just not step on our gowns?", user_id=4),
        Post(id=5, content="A happy meal.", user_id=5),
        Post(id=6, content="According to my jet lag it is one hundred o clock celsius.", user_id=4),
        Post(id=7, content="I come back stronger than a 90’s trend", user_id=3),
        Post(id=8, content="the evermore deluxe album with 2 bonus tracks “right where you left me” and “it’s time to go” is now available", user_id=2),
        Post(id=9, content="bye 2020, it’s been weird.", user_id=1),
        Post(id=10, content="Guys. Seriously. Thank you for doing this.", user_id=2),
        Post(id=11, content="Footage of evermore, folklore and lover hearing this news ", user_id=3),
        Post(id=12, content="I need nothing else for my birthday this year. Or any other year. Ever. This is it. I love you Dolly", user_id=4),
        Post(id=13, content="This review turned me into an actual weeping willow, thank you", user_id=5),
        Post(id=14, content="Tonight the story continues, as the music video for “willow” drops at midnight eastern.", user_id=4),
        Post(id=15, content="Over here in folkloreland we feel great about it. Thanks @latimes!", user_id=3),

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()