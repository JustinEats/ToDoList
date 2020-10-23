from app import app
from models import db, ToDoList

db.delete_all()
db.create_all()

first = ToDoList(task="Clean stove", description="Needs to be washed down throughly.")
second = ToDoList(task="Do Laundry", description="Three loads need to be washed.")
third = ToDoList(task="Excercise", description="Need to get them gains.")

db.session.add_all([first,second,third])
db.session.commit()