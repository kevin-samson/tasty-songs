from flask import Flask
from flask_socketio import SocketIO
from config import Config
import spotipy

sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=Config.CLIENT_ID, client_secret=Config.CLIENT_SECRET,
                                       redirect_uri=Config.REDIRECT_URI,
                                       scope=Config.SCOPE)


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from .views import view

        # REGISTER ROUTES
        app.register_blueprint(view, url_prefix="/")
        socketio = SocketIO(app)
    return app, socketio
