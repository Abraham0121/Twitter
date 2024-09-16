from flask import Flask, jsonify, flash, request, redirect, render_template, session
import requests, json
from models import User, Tweet, db


app=Flask(__name__)
app.app_context().push() 



app.config["SQLALCHEMY_DATABASE_URI"]="postgresql://postgres@localhost:5432/twitter_database"
app.config['SECRET_KEY'] = "secret"
app.config["DEBUG"] = True

db.init_app(app)
db.create_all()

# app.register_blueprint(main)




@app.route('/')
def homepage():
    if 'username' in session:
        user = User.query.get(session['username'])
        print(user,"HELLO")
        return render_template('home.html', user=user)
    # tweets = Tweet.query.filter_by()

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username, password=password).one_or_none()
        if existing_user:
            session['username'] = username
            flash('You are logged in', 'success')
            return redirect('/')
        else:
            flash('That password username combination is invalid', 'danger')
            return render_template('login.html')
        
@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
        flash('You have successfully logged out', 'success')
        return redirect('/')
    else:
        flash('You have not logged in', 'danger')
        return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        username = request.form['username']
        existing_user = User.query.get(username)
        if existing_user:
            flash('This user already exists', 'danger')
            return render_template('register.html')
        else:
            user = User(
                username=request.form['username'],
                password=request.form['password']
            )

            db.session.add(user)
            db.session.commit()
            flash('You have been added to the database', 'success')
            session['username'] = username
            return redirect('/')

@app.route('/profile')
def profile():
    if 'username' in session:
        user = User.query.filter_by(session['username'])
        return render_template('profile.html', user=user)
    
    return render_template('profile.html')

