from App.models import User
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask_login import login_required, login_user, current_user, logout_user


from.index import index_views

from App.controllers import (
    create_user,
    create_profile,
    add_ranking,
    get_user_by_username,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    jwt_required, 
    get_user_competitions,
    login

)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/users', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return render_template('users.html', users=users)

#this was commented off

@user_views.route('/api/users', methods=['GET'])
@jwt_required()
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'], data['email'])
    user_id = get_user_by_username(data['username'])
    create_profile(user_id.id, data['username'])
    add_ranking(user_id.id, data['username'])
    return jsonify({'message': f"user {data['username']} created"}), 201
    