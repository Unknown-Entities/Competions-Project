from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    get_rankings_json,
    get_top_20_users_rank
)

rank_views = Blueprint('rank_views', __name__, template_folder='../templates')

@rank_views.route('/rankings', methods=['GET'])
@jwt_required()
def get_rankings_action():
    check = get_rankings_json()
    return jsonify(get_rankings_json()), 200

@rank_views.route('/rankings/20', methods=['GET'])
@jwt_required()
def get_top_rankings_action():
    check = get_top_20_users_rank()
    return jsonify(check), 200
