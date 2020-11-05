from flask import Flask, render_template, request, flash
from models import db, connect_db, User, ToDoList
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
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.password.data
        new_user = User.register(username, password, email)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
    return render_template('signup.html', form=form)