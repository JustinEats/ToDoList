from flask import Flask, render_template, request
from models import db, connect_db, ToDoList
from forms import RegisterUser, LoginUser, ToDoList
from secrets import KEY

app = Flask (__name__)
app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///ToDoList'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup')
def signup():
    form = RegisterUser()
    return render_template('signup.html', form=form)