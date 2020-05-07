from app import app
from flask import json, render_template, request
from markupsafe import escape
from neural_net import cnn_model as nnet


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

