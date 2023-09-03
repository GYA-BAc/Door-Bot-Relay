"""
The bot host, meant to be run on an external server to bypass any wifi restrictions
Meant to be used with a reciever, which will connect to the hoster instead of directly to discord, thereby bypassing restrictions
"""

import subprocess
from flask import Flask



if __name__ == '__main__':

    # flask app hosting
    app = Flask(__name__)
    
    @app.route('/')
    # ‘/’ URL is bound with hello_world() function.
    def counter():

        try:
            with open("tmp", "r") as file:
                count: str = file.read()

            return count
        except Exception:
            return "0"


    # open bot as subprocess
    try:
        bot_process = subprocess.Popen(["python", "bot.py"])
    except Exception:
        # try another python alias
        bot_process = subprocess.Popen(["python3", "bot.py"])

    try:

        app.run()

    except: # bare except to catch KeyboardInterrupt too
        bot_process.kill()
