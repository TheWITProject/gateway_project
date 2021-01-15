from app import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(30))
    posts = relationship("Post", back_populates='user')
    
    def serialize(self):
        return {}


class Post(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    content = Column(String(280))
    
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

    def serialize(self):
        return {}