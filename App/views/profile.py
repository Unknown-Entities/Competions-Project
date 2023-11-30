from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    create_profile,
    get_profile,
    update_profile,
    findCompUser
)

profile_views = Blueprint('user_competition_views', __name__, template_folder='../templates')

@profile_views.route('/profile', methods=['POST'])
@jwt_required()
def create_profile_action():
    data = request.json
    if jwt_current_user.is_admin:
        comp = create_profile(profileID=data['profileID'], studentID=data['studentID'], name=data['name'],university=data[university])
        if comp:
            return jsonify({"message": f"Profile created with id {comp.profileid}"}), 201
        return jsonify({"error": f"Profile {data['profileID']} already exists "}), 500
   

@profile_views.route('/profile', methods=['GET'])
@jwt_required()
def get_profile_action():
    check = get_profile_json()
    return jsonify(get_profile_json()), 200