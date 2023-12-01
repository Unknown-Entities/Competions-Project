from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    #create_profile,
    get_profile,
    get_profile_ranking,
    get_user_competitions,
    jwt_required,
    #update_profile,
    findCompUser
)

profile_views = Blueprint('profile_views', __name__, template_folder='../templates')
   
@profile_views.route('/profile/<int:id>', methods=['GET'])
@jwt_required()
def get_profile_action(id):
    profile = get_profile(id)
    comps = get_user_competitions(id)
    rank = get_profile_ranking(id)
    return (jsonify(profile.toJSON(), comps)), 200