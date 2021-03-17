from flask import session
from flask_socketio import SocketIO
import time
from application import create_app
import config

# SETUP
app = create_app()
socketio = SocketIO(app)  # used for user communication


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    for i in range(10):
        socketio.emit('message response', i)


if __name__ == "__main__":  # start the web server
    socketio.run(app, debug=True, host=str(config.Config.SERVER))
