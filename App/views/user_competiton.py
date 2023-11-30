from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    create_competition_user,
    get_competition_user,
    update_competition_user,
    findCompUser
)

user_competition_views = Blueprint('user_competition_views', __name__, template_folder='../templates')

@user_competition_views.route('/user_competition', methods=['POST'])
@jwt_required()
def create_competition_user_action():
    data = request.json
    if jwt_current_user.is_admin:
        comp = create_competion_user(username=data['username'], password=data['password'], email=data['email'])
        if comp:
            return jsonify({"message": f"Competition User created with id {comp.id}"}), 201
        return jsonify({"error": f"Competition {data['username']} already exists "}), 500
   

@user_competition_views.route('/user_competitions', methods=['GET'])
@jwt_required()
def get_competition_user_action():
    check = get_competition_user_json()
    return jsonify(get_competition_user_json()), 200