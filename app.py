from flask import Flask, render_template, url_for, redirect, request, session
from flask_session import Session
import logging
import random, string, json
from settings import LOG_FILE, SECRET_KEY, PASSWORD, SESSION_TYPE
from services import upload_to_s3

app = Flask(__name__)
app.config.from_object(__name__)
Session(app)
# logging.basicConfig(filename=LOG_FILE,level=logging.DEBUG)

# TODO:
# - add logging


# home page with upload region
@app.route('/', methods=['GET','POST'])
def index():
    # check if logged in, else direct to login page
    if 'token' in session and session.get('token') == SECRET_KEY:
        session['token'] = SECRET_KEY
        if request.method=='GET':
            return render_template('index.html')

        if request.method=='POST':
            return upload_to_s3(request.files['file'])
    else:
        session['token'] = SECRET_KEY
        return render_template('index.html')
        # return redirect('/login_page')

# route to login page, redirects to home if logged in
@app.route('/login_page')
def login():
    # if logged in, redirect to 
    if 'token' in session and session.get('token') == SECRET_KEY:
        return redirect('/')
    else:
        # return render_template('login.html')
        return render_template('login.html')
    return 200

@app.route('/logout')
def logout():
    return 200

# after upload feedback
@app.route('/done')
def done():
    return 200

if __name__ == "__main__":
  app.run(debug=True)