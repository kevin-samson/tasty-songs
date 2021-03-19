from flask import Blueprint
from flask import render_template, session, redirect, request, url_for
from application import sp_oauth
import time
from config import Config

view = Blueprint("views", __name__)


@view.route('/')
def home():
    return render_template('index.html')


@view.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        return redirect('verify')
    return render_template('login.html')


@view.route("/verify")
def verify():
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@view.route("/api_callback")
def api_callback():
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code, check_cache=False)

    session["token_info"] = token_info
    return redirect('/')


def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if is_token_expired:
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid
