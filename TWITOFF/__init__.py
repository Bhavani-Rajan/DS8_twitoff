""" Entry point for our twitoff flask app"""
from .app import create_app

#APP is a global varible
APP = create_app()

#run this in teerminal with FLASK_APP=TWITOFF:APP flask run
