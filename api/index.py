from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "HydroSentinel Advanced is LIVE! Fixed!"

@app.route('/api/test')
def test():
    return "API Working!"
