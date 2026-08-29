from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "HydroSentinel Advanced is LIVE! 404 Fixed!"

@app.route('/<path:path>')
def catch_all(path):
    return f"Page {path} - HydroSentinel Working!"
