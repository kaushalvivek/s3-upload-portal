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
        if request.method=='GET':
            return render_template('index.html')

        elif request.method=='POST':
            session['upload_message'] = upload_to_s3(request.files['file'])
            return redirect('/done')
    else:
        return redirect('/login_page')

# route to login page, redirects to home if logged in
@app.route('/login_page', methods=['GET','POST'])
def login():
    # if logged in, redirect to home
    if 'token' in session and session.get('token') == SECRET_KEY:
        return redirect('/')
    else:
        if request.method=='GET':
            return render_template('login.html', error=False)

        elif request.method=='POST':
            if request.form['password'] == PASSWORD:
                session['token']=SECRET_KEY
                return redirect('/')
            else:
                return render_template('login.html', error=True)

@app.route('/logout')
def logout():
    session.pop('token')
    return redirect('/login_page')

# after upload feedback
@app.route('/done')
def done():
    return session['upload_message']

if __name__ == "__main__":
  app.run(debug=True)