from os import environ
from Bard import Chatbot
from flask import Flask, request, render_template, redirect

server = Flask(__name__)

# get token
token = environ.get("BARD_TOKEN")

# init chatbot
chatbot = Chatbot(token)

def generate_response(prompt):
    try:
        response = chatbot.ask(prompt)
        return response
    except Exception as e:
        return e

@server.route("/")
def home():
    return render_template("chat.html")

@server.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
