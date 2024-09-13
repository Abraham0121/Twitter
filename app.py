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
        return render_template('home.html', user=user)
    # tweets = Tweet.query.filter_by()

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/profile')
def profile():
    user = User.query.filter_by(session.username)

    return render_template('profile.html', user=user)

