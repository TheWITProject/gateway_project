from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable= False) 
    posts = db.relationship("Post", back_populates="users")
    

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username
        }


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(280), nullable=False) 
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("User", back_populates="posts")

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "users_id":self.users_id,
            "users":self.users.username

        }