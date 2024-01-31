'''this module creates a blueprint for all endpoints'''
from flask import Blueprint

app_views = Blueprint('app_views', __name__)


from api.v1.views.route import * 
