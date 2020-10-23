from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class ToDoList(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    checked = db.Column(db.Boolean, default=False)

    def __repr__(self):
        self = t
        return f"<ToDoList {t.task}, {t.checked}>"
