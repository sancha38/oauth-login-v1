
from flask import Flask,redirect,session,request,send_from_directory,render_template
from authlib.integrations.flask_client import OAuth
from flask import url_for, render_template
from flask import jsonify, request
#from authlib.flask.client import OAuth
import json
import os



app = Flask(__name__,static_url_path='')

app.secret_key = 'yxrtnvdyyioke'
oauth = OAuth(app) 

git = oauth.register(
    'git',
    client_id="da1034bbe7aa3ba5653b",
    client_secret="3ade3058e2023e0f9ee9700849acbfbcbabc6e02",
    authorize_url="https://github.com/login/oauth/authorize",    
    client_kwargs={'scope': 'user,public_repo'},
    access_token_url="https://github.com/login/oauth/access_token",
    api_base_url = "https://api.github.com/"
)
@app.route('/login')
def login():
    git  = oauth.create_client('git')
    redirect_uri = url_for('authorize', _external=True)
    return git.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():

    p = request.args.to_dict(flat=True)
    git  = oauth.create_client('git')   
    token = git.authorize_access_token()
    print(token)
    resp = git.get('user')
    print(resp)
    profile = resp.json()
    print(profile)
    # do something with the token and profile
    return redirect('/')

@app.route('/<path:path>')
def send_js(path):
    #print(app.static_folder)
    
    return send_from_directory(app.static_folder, path)

@app.route("/process/<path:path>") 
def proc_list(path): 
    print(path)
    print(app.static_folder)
    
    return render_template('index.html')


@app.route("/") 
def home_view(): 
    print("home")
    print(app.static_folder)
    return render_template('index.html')

@app.route("/api_watch/services/processmeta",methods = ['POST']) 
def process(): 
    params = get_params(request)
    print("process",params)
    proc_id = params.get("proc_id",-1)
    filep = os.path.join(app.static_folder,'assets/json/','process.json')
    print("filep ",filep)
    with open(filep) as f:
        data = json.load(f)
        return jsonify(data.get(proc_id,{}))
    


@app.route("/api_watch/services/processinstance",methods = ['POST']) 
def step(): 
    params = get_params(request)
    print("step",params)
    proc_id = params.get("process_id",-1)
    filep = os.path.join(app.static_folder,'assets/json/','step.json')
    print("filep ",filep)
    with open(filep) as f:
        data = json.load(f)
        d =data.get(proc_id,{})
        print(d)
        return jsonify(d)


def get_params(request):
        return request.json if (request.method == 'POST') else request.args




