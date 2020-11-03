from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(30), nullable=False, unique=True)
    password=db.Column(db.String(30), nullable=False)
    email=db.Column(db.Text, nullable=False)

    def __repr__(self):
        self = u
        return f"<ToDoList {u.task}, {u.checked}>"


class ToDoList(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, ForeignKey('users.id'))

    user = db.relationship('User', backref='todo')

    def __repr__(self):
        self = t
        return f"<ToDoList {t.task}, {t.checked}>"

def connect_db(app):
    db.app = app
    db.init_app(app)