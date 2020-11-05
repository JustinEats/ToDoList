from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(length=30), nullable=False, unique=True)
    password=db.Column(db.String(length=30), nullable=False)
    email=db.Column(db.Text, nullable=False)

    @classmethod 
    def register(cls, username, password, email):
        hashed = bcrypt.generate_password_hash(password)
        hashed_utf8 = hashed.decode('utf-8')
        return cls(username=username, password=hashed_utf8, email=email)

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False

    def __repr__(self):
        self = u
        return f"<User {u.username}, {u.email}>"


class ToDoList(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User', backref='todo')

    def __repr__(self):
        self = t
        return f"<ToDoList {t.task}, {t.checked}>"

def connect_db(app):
    db.app = app
    db.init_app(app)