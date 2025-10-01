"""
Initialize the Flask application package.
"""

from flask import Flask
import combat_creator_1api.views

app = Flask(__name__)
