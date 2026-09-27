from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models import db, User, Favorite
from tool_registry import get_tool_by_id

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('user_id'):
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not username or not email or not password:
            flash('All fields are required.', 'danger')
            return render_template('auth/register.html')

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('auth/register.html')

        if User.query.filter_by(username=username).first():
            flash('Username is already taken.', 'danger')
            return render_template('auth/register.html')

        if User.query.filter_by(email=email).first():
            flash('Email is already registered.', 'danger')
            return render_template('auth/register.html')

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        session['user_id'] = user.id
        session['username'] = user.username
        flash('Account created successfully! Welcome to ToolHub.', 'success')
        return redirect(url_for('main.index'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_id'):
        return redirect(url_for('main.index'))

    if request.method == 'POST':
        email_or_user = request.form.get('login_id', '').strip()
        password = request.form.get('password', '')

        user = User.query.filter(
            (User.email == email_or_user.lower()) | (User.username == email_or_user)
        ).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Welcome back, {user.username}!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username/email or password.', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('main.index'))

@auth_bp.route('/profile')
def profile():
    user_id = session.get('user_id')
    if not user_id:
        flash('Please login to view your profile.', 'warning')
        return redirect(url_for('auth.login'))

    user = User.query.get(user_id)
    fav_records = Favorite.query.filter_by(user_id=user_id).all()
    favorite_tools = [get_tool_by_id(f.tool_id) for f in fav_records if get_tool_by_id(f.tool_id)]

    return render_template('auth/profile.html', user=user, favorite_tools=favorite_tools)
