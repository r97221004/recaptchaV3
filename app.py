from flask import Flask, render_template, redirect, url_for, request
import requests


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/sign-user-up", methods=['POST'])
def sign_up_user():
    res = request.form['email']
    print(res)
    return redirect(url_for('index'))
