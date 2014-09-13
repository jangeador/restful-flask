#!flask/bin/python
from flask import Flask, jsonify, redirect, url_for
from werkzeug.contrib.fixers import ProxyFix
from decorators import crossdomain
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

engine = create_engine('sqlite:///db.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
# Models:


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

    def as_dict(self):
        return {'id': self.id,
                'title': self.title,
                'description': self.description,
                'done': self.done}


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)

    # for task in tasks:
    #     print(task)
    #     t = (Task(task['title'], task['description']))
    #     db_session.add(t)
    # db_session.commit()



@app.route('/')
def index():
    return redirect(url_for('get_tasks'))


# @app.route('/todo/api/v1.0/tasks', methods = ['GET'])
@app.route('/tasks', methods=['GET'])
@crossdomain(origin='*')
def get_tasks():
    all_tasks = Task.query.all()
    print(all_tasks)
    return jsonify({'tasks': [a.as_dict() for a in all_tasks]})

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)


