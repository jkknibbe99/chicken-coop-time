# Imports
import json, datetime
from flask import Flask, render_template, request, redirect, url_for



###############################################
#        Define flask app and Globals         #
###############################################


# Initialize app
app = Flask(__name__)
app.config['DEBUG'] = True




###############################################
#              Routes                         #
###############################################


@app.route('/')
def index():
    """
    Main route. Displays current datetime
    """
    dt = datetime.datetime.now()
    print(dt)
    return render_template('index.html', datetime=dt)




###############################################
#                Start the App                #
###############################################


def start(dev:bool):
    app.run(port=5000, host='0.0.0.0', debug=dev)
