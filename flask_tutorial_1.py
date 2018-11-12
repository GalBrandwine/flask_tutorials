from flask import Flask
app = Flask(__name__)

# A comment
@app.route('/')
def hello_world():
    return 'Hello, World!'