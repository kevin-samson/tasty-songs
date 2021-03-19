from flask import session, redirect
from application.views import get_token
import spotipy
import json
from application import create_app
import config

# SETUP
app, socketio = create_app()


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


@socketio.on('search song')
def handle_song(data):
    print(str(data))
    session['token_info'], authorized = get_token(session)
    session.modified = True
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    socketio.emit('song data', sp.search(q=data['data'], type='track'))


if __name__ == "__main__":
    socketio.run(app, debug=True, host=str(config.Config.SERVER))
