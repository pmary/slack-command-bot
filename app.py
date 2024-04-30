import os
from dotenv import load_dotenv
from flask import Flask, request
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

app_token = os.getenv('SLACK_APP_TOKEN')
bot_token = os.getenv('SLACK_BOT_TOKEN')
app_signing_secret = os.getenv('SLACK_APP_SIGNING_SECRET')

bolt_app = App(token = bot_token, signing_secret=app_signing_secret)
flask_app = Flask(__name__)
handler = SlackRequestHandler(bolt_app)

@bolt_app.command("/redalert")
def custom_command_function(ack, respond, command):
    ack()
    #TODO implement the logic 
    respond("your message") # if it is needed

@flask_app.route("/", methods=["POST"])
def slack_events():
    return handler.handle(request)

if __name__ == '__main__':
    #main()
    flask_app.run(host='0.0.0.0', port=3000)