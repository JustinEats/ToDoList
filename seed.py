from app import app
from models import db, ToDoList

db.drop_all()
db.create_all()