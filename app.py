from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return "cant find token on given download id"

@app.route('/<id>')
def id(id):
    try:
        r = requests.get(url = "https://bowfile.com/" + id, headers = {"Cookie": "filehosting=20nupilfrt7df5b8hurj69prio"})
        token = r.text.split("showFileInformation(")[1].split(");")[0]
    except:
        return "cant find token on given download id"
    ddl = requests.request('HEAD', url = "https://bowfile.com/account/direct_download/" + token, headers = {"Cookie": "filehosting=20nupilfrt7df5b8hurj69prio"}) 
    return redirect(ddl.url)