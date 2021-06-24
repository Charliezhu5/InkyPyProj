from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/clean')
def clean():
    os.system("sudo python3 clean.py")
    return 'Cleaned!'

@app.route('/pic/<PNGname>')
def show_logo(PNGname):
    os.system(f'sudo python3 drawPNG.py --name {PNGname}')
    return 'Showing Picture!'

@app.route('/namebadge/<name>')
def namebadge(name):
    os.system(f'python3 name-badge.py --type "auto" --colour "red" --name "{name}"')
    return f'Showing {name} on name badge!'