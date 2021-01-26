from models import User, Post
import datetime

def seed(db):
    users = [User(id = 1, username = "ilovedogs"),
    User(id = 2, username = "shiv123"),
    User(id = 3, username = "svnyc12"),
    User(id = 4, username = "doggos4evr"),
    User(id = 5, username = "sushilover34")

    ]

    posts = [Post(id = 1, content = "Hi everyone!", user_id = 1),
    Post(id = 2, content = "I'm tired.", user_id = 2),
    Post(id = 3, content = "26% of computing-related jobs are held by women" , user_id = 3),
    Post(id = 4, content = "Women of color, only make up 18%% of entry-level positions, as opposed to 30%% of white women and 35%% of white men." , user_id = 1),
    Post(id = 5, content = "50%% of women said they have experienced gender discrimination at work.", user_id = 3),
    Post(id = 6, content = "Women software engineer hires have only increased 2%% over the last 20 years." , user_id = 2),
    Post(id = 7, content = "Just 3% of computing-related jobs are held by African-American women, 6%% held by Asian women and 2%% held by Hispanic women", user_id = 3),
    Post(id = 8, content = "The five largest tech companies on the planet (Amazon, Apple, Facebook, Google and Microsoft) only have a workforce of about 34.4% women.", user_id = 2),
    Post(id = 9, content = "40%% of US businesses are owned by women, with 64%% of new women-owned businesses being started by women of color.", user_id = 1),
    Post(id = 10, content = "Women currently remain highly underrepresented in software engineering (14%% of total workforce) and computer science-related jobs (25%% of total workforce).", user_id = 3),
    Post(id = 11, content = "48%% of women in STEM jobs report discrimination in the recruitment and hiring process", user_id =2),
    Post(id = 12, content = "40%% of US businesses are owned by women, with 64%% of new women-owned businesses being started by women of color.", user_id = 1),
    Post(id = 13, content = "Goodnight", user_id = 5)

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()