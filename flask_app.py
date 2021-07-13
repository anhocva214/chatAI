from flask import Flask, request
from chat import InputChat

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/api/chat', methods=['POST'])
def Chat():
    message = request.form['message']
    reply = InputChat(message)
    return reply

# app.run()