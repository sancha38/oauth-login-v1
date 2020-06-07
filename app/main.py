
from flask import Flask,redirect,session,request
from authlib.integrations.flask_client import OAuth
from flask import url_for, render_template
#from authlib.flask.client import OAuth


app = Flask(__name__) 
app.secret_key = 'yxrtnvdyyioke'
oauth = OAuth(app) 

git = oauth.register(
    'git',
    client_id="da1034bbe7aa3ba5653b",
    client_secret="3ade3058e2023e0f9ee9700849acbfbcbabc6e02",
    authorize_url="https://github.com/login/oauth/authorize",    
    client_kwargs={'scope': 'user,public_repo'},
    access_token_url="https://github.com/login/oauth/access_token"
)

@app.route("/") 
def home_view(): 
    print("session ",session)
    d = dict(session)
    print(d)
    return "<h1>Welcome to Geeks for Geeks</h1>"



@app.route('/login')
def login():
    git  = oauth.create_client('git')
    redirect_uri = url_for('authorize', _external=True)
    return git.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    p = request.args.to_dict(flat=True)
    print(p)
    git  = oauth.create_client('git')
    token = git.authorize_access_token()
    print(token)
    resp = git.get('user')
    print(resp)
    profile = resp.json()
    print(profile)
    # do something with the token and profile
    return redirect('/')
