from flask import session
from flask_socketio import SocketIO
import time
from application import create_app
import config

# SETUP
app = create_app()
socketio = SocketIO(app)  # used for user communication


if __name__ == "__main__":  # start the web server
    socketio.run(app, debug=True, host=str(config.Config.SERVER))
