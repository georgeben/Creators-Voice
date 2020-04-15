from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
def home_page():
  return 'Welcome to creators voice'
app.run(host= '0.0.0.0', port=environ.get('PORT'))