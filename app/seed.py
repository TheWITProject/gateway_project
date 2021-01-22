from models import User, Post
import datetime

def seed(db):
    users = [
        User(id=1, username="MyNameIsJoshInHisPhone"),
        User(id=2, username="iLooklikeYES&youLooklikeNO"),
        User(id=3, username="SleepingInTheBackofClass"),
        User(id=4, username="UrValedictorian"),
        User(id=5, username="ReportingLive"),

    ]

    posts = [

                Post(id=1, content= """Make sure to buy your tickets for the Homecoming Dance. The theme is A Night to Remember.Whether you are going with your boo thang or by yourself  
            this is a night you won't want to miss""", user_id=5 ),
        Post(id=2, content= """Congratulations to Mrs. Thomas and Mr. Chang for welcoming their newborn baby girl into the world. When you have a mom who is a calculus techer  
            and a dad who teaches AP English, Let's just say she is all set""", user_id=5 ),
        Post(id=3, content= """A message from our lovely custodial staff, Please stop flushing bananas down the boys bathroom toilets. Its damaging the pipes. We 
            still not have caught the Banana Boys but when we do they will face serious consequences""", user_id=5 ),
        Post(id=4, content= "Can anyone give me advice on which teacher to pick for Calc BC. I'm scared of getting a bad teacher", user_id=4 ),
        Post(id=5, content= "The National Honor Society will be having a meeting after school today in the auditorium. Pleade don't be late", user_id=4 ),
        Post(id=6, content= "I don't think I'm crazy, but I don't understand how I only got into six Ivy League schools.", user_id=4 ),
        Post(id=7, content= "BRRRRROOO Stop flushing bananas down the freaking toilets. Who raised ya'll", user_id=3 ),
        Post(id=8, content= "Tell me how I copied someone's homeowrk for physics and they got a higher score than me", user_id=3 ),
        Post(id=9, content= "I really be giving Ms. Sanchez a blank look when she asks me something in spanish. I do understand when she be like para la tarea tho", user_id=3 ),
        Post(id=10, content= """Girls be so scared to put an at like stop talking about people like it's your day job. In fact get a real one to pay for better 
            hair extentions""", user_id=1 ),
        Post(id=11, content= """Others may say you look like trash, you have no fashion sense, you have bad makeup skills, you have no talent, and all you do is 
            talk about people since you have nothing better to do. But honey they are wrong. You don't have bad makeup skills.""", user_id=1 ),
        Post(id=12, content= """Not people out here boasting about possible swiping their sugar daddy's credit card. We all know in your mind your praying 
            it doesnt decline. Only hurt dogs holler so I''l just be sitting pretty in the corner""", user_id=1 ),
        Post(id=13, content= "I really just be scrolling through my feed and finding out how much propoerty I own in some people's heads LOL", user_id=2 ),
        Post(id=14, content= "Some of you need a job as a maid since you do so well digging through my trash. By the way sweetie your face is scary enoguh for me", user_id=2 ),
        Post(id=15, content= """The pretty just get prettier and the haters keep hating. Only one of those statements apply to me. In the future, I cant wait  
            until you have to swipe my black card for the two Chanel bags I just bought. Babe I just spent your rent money on some bags""", user_id=2 ),

    ]

    db.session.add_all(users)
    db.session.add_all(posts)
    db.session.commit()
