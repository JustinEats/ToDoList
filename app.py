from flask import Flask, render_template, flash, url_for, session, redirect
from models import db, connect_db, User, ToDoList
from forms import RegisterUser, LoginUser, ToDoForm
from secrets import KEY
from flask_debugtoolbar import DebugToolbarExtension

app = Flask (__name__)
app.config['SECRET_KEY'] = KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///ToDoList'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False

connect_db(app)
debug = DebugToolbarExtension(app)

@app.route('/')
def home():
    user = User.query.all()
    return render_template('home.html', user=user)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterUser()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        new_user = User.register(username, password, email)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        return redirect(url_for('user_profile', id=new_user.id))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginUser()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        login_user = User.authenticate(username,password)
        if login_user:
            session['user_id'] = login_user.id
            return redirect(url_for('user_profile', id=login_user.id))
        else:
            flash('Invalid Username/Password')
    return render_template('login.html', form=form)

@app.route('/account/<int:id>', methods=["GET", "POST"])
def user_profile(id):
    user = User.query.get_or_404(id)
    todos = ToDoList.query.all()
    form = ToDoForm()
    if form.validate_on_submit():
        todo = form.todo.data
        new_todo = ToDoList(task=todo, user_id=id)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('user_profile', id=user.id))
    return render_template('user-profile.html', user=user, todos=todos, form=form)

@app.route('/logout')
def logout_user():
    session.pop('user_id')
    return redirect('/')

@app.route('/todo/<int:id>/edit', methods=["GET", "POST"])
def edit_todo(id): 
    todo_edit = ToDoList.query.get_or_404(id)
    form = ToDoForm(obj=todo_edit)
    if form.validate_on_submit():
        todo_edit.task = form.todo.data
        new_edit = ToDoList(task=todo_edit, user_id = session["user_id"])
        db.session.commit()
        return redirect(url_for('user_profile', id= session["user_id"]))
    return render_template('edit-todo.html', form=form)

@app.route('/todo/<int:id>/delete', methods=["POST"])
def delete_todo(id):
    todo = ToDoList.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('user_profile', id=session["user_id"]))
    # return render_template('user-profile.html')
