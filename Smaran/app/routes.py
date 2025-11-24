from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from datetime import datetime
from . import db
from .models import User, Task


main = Blueprint('main', __name__)
@main.route('/test')
def test():
    return "<h1>SMARAN IS WORKING!</h1>"
# --- AUTH ---
@main.route('/')
def index():
    return redirect(url_for('main.login'))

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.dashboard'))
        flash('Invalid Credentials')
    return render_template('login.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if User.query.filter_by(username=username).first():
            flash('Username taken')
            return redirect(url_for('main.register'))
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html')

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

# --- PLANNER LOGIC ---
@main.route('/dashboard')
@login_required
def dashboard():
    # Fetch tasks and sort by deadline (soonest first)
    tasks = Task.query.filter_by(user_id=current_user.id, is_completed=False).order_by(Task.deadline.asc()).all()
    completed = Task.query.filter_by(user_id=current_user.id, is_completed=True).order_by(Task.deadline.desc()).limit(5).all()
    
    current_time = datetime.now()
    
    return render_template('dashboard.html', tasks=tasks, completed=completed, now=current_time)

@main.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    category = request.form.get('category')
    date_str = request.form.get('date')
    time_str = request.form.get('time')
    
    # Combine Date and Time
    dt_string = f"{date_str} {time_str}"
    deadline_obj = datetime.strptime(dt_string, '%Y-%m-%d %H:%M')
    
    new_task = Task(title=title, category=category, deadline=deadline_obj, owner=current_user)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/complete/<int:id>')
@login_required
def complete_task(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        task.is_completed = True
        db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/delete/<int:id>')
@login_required
def delete_task(id):
    task = Task.query.get(id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.dashboard'))