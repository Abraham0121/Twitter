from flask import Flask, jsonify, flash, request, redirect, render_template, session
import requests, json


app=Flask(__name__)
app.app_context().push() 

# app.config["SQLALCHEMY_DATABASE_URI"]
app.config['SECRET_KEY'] = "secret"
app.config["DEBUG"] = True

# app.register_blueprint(main)




@app.route('/')
def homepage():

    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    return render_template('login.html')

@app.route('/register')
def register():

    return render_template('register.html')

@app.route('/profile')
def profile():

    return render_template('profile.html')

