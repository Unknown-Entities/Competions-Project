from App.models.user import User
from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from flask_login import login_required, login_user, current_user, logout_user


from.index import index_views

from App.controllers import (
    create_user,
    jwt_authenticate, 
    get_all_users,
    get_all_users_json,
    jwt_required, 
    get_ranked_users,
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
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))

@user_views.route('/static/users', methods=['GET'])
def static_user_page():
  return send_from_directory('static', 'static-user.html')


@user_views.route('/normal', methods=['POST'])
def create_normal_user_action():
    data = request.json
    check = User.query.filter_by(username=data['username']).first()
    if not check:
        result = create_user(username=data['username'], password=data['password'], email=data['email'])
        if result:
            return jsonify({"message": f"User created with id {result.id}"}), 201
    return jsonify({"error": f"Username {data['username']} already exists "}), 500


@user_views.route('/users/rankings', methods=['GET'])
def get_user_rankings():
    users = get_ranked_users()
    rankings = [u.to_dict() for u in users]
    return jsonify(rankings)

@user_views.route('/users/competitions/<int:id>', methods = ['GET'])
def get_user_comps(id):
    data = request.form
    # comps = get_user_competitions(data['id'])
    comps = get_user_competitions(id)
    # userCompetitions =  [c.toDict() for c in comps]
    return jsonify(comps)
    