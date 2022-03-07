from flask import Flask, redirect, render_template, request, send_from_directory
import requests, validators, os
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/<path>')
def to_index(path):
    return redirect("/")

@app.route('/api')
def api():
    args = request.args
    if "url" not in args:
       return redirect("/")
    if validators.url(args.get("url")):
        if args.get("url").startswith("https://bowfile.com/"):
            id = args.get("url").replace("https://bowfile.com/", "")
            r = requests.get(url = "https://bowfile.com/" + id, headers = {"Cookie": "filehosting=20nupilfrt7df5b8hurj69prio"})
            try:
                token = r.text.split("showFileInformation(")[1].split(");")[0]
            except:
                return redirect("/")
            ddl = requests.request('HEAD', url = "https://bowfile.com/account/direct_download/" + token, headers = {"Cookie": "filehosting=20nupilfrt7df5b8hurj69prio"}) 
            return redirect(ddl.url)
    return redirect("/")