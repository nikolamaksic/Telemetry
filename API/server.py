import os
from app import create_app
from config.development import Development
import flask


""" Instantiate the Application singleton by passing the aliased development
    configuration class to the App Factory function
"""
app = create_app(Development)



@app.route('/')
def hello():
    return 'Hello!'

