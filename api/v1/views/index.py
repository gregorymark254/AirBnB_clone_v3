#!/usr/bin/python3
"""
contains the app blueprints
"""
from api.v1.views import app_views
from flask import jsonify
from ..app import app
from models.engine.db_storage import *

@app_views.route('/status')
def status():
    """return the status of the api"""
    return jsonify({"status": "OK"})

@app.route('/api/v1/stats')
def retrieve():
    """returns the no. of items in classes"""
    new_dict = {}
    for obj in classes:
        total = count(obj)
        new_dict[obj] = total
    return jsonify(new_dict)
