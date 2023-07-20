from os import environ
from Bard import Chatbot
from flask import Flask, request, render_template

server = Flask(__name__)

# get token
Secure_1PSID = environ.get("BARD__Secure-1PSID")
Secure_1PSIDTS = environ.get("BARD__Secure-1PSIDTS")

# init chatbot
chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

def generate_response(prompt):
    try:
        response = chatbot.ask(prompt)
        return response["content"]
    except BaseException as e:
        return str(e)

@server.route("/")
def home():
    chatbot.conversation_id = ""
    chatbot.response_id = ""
    chatbot.choice_id = ""
    return render_template("chat.html")

@server.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return str(generate_response(user_text))

if __name__ == '__main__':
    server.run(debug=False, host='0.0.0.0', port=8088)
