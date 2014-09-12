from sqlalchemy import Column, Integer, String, Boolean
from server.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(String(1024))
    done = Column(Boolean)

    def __init__(self, title=None, description=None, done=False):
        self.title = title
        self.description = description
        self.done = done

    def __repr__(self):
        return '<Title %r>' % (self.title)