from flask import Flask, render_template, redirect, url_for, request, abort
import requests


app = Flask(__name__)

SITE_KEY = '6LfxYGMjAAAAAHJInOuVwxBIhV4gyunkZfUeNkO7'
SECRET_KEY = '6LfxYGMjAAAAAAvYR0mYNySs4NP9FzHyQ0xMnDj3'
VERIFY_URL = 'https://www.google.com/recaptcha/api/siteverify'


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html', site_key=SITE_KEY)


@app.route("/sign-user-up", methods=['POST'])
def sign_up_user():
    secret_response = request.form['g-recaptcha-response']

    verify_response = requests.post(
        url=f'{VERIFY_URL}?secret={SECRET_KEY}&response={secret_response}').json()

    print('verify_response: ', verify_response)

    if verify_response['success'] == False or verify_response['score'] < 0.5:
        abort(401, 'you are a robot.')

    return redirect(url_for('index'))
