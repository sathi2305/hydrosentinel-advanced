from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "HydroSentinel Advanced is LIVE!"

@app.route('/dashboard')
def dashboard():
    return "Dashboard Working!"

@app.route('/<path:path>')
def all_routes(path):
    return f"Route {path} is working!"
