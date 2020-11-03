from flask import Flask, render_template, request
from models import db, connect_db, ToDoList
from secrets import KEY

app = Flask (__name__)
app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///ToDoList'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

