from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    # create_user,
    # jwt_authenticate, 
    # get_all_users,
    # get_all_users_json,
    create_admin,
    jwt_required,
    create_competition,
    get_all_competitions_json,
    get_competition_by_id,
    add_results,
    get_user_rankings,
    add_user_to_comp
)

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

#@admin_views.route('/users', methods=['POST'])
#def create_admin():
#    data = request.form
#    flash(f"User {data['username']} created!")
    #create_admin(data['username'], data['password'])
#    newAdmin = Admin(create_user(data['username'], data['password']))
#    return newAdmin

@admin_views.route('/api/admin', methods=['POST'])
def create_admin_action():
    data = request.json
    create_admin(data['username'], data['password'], data['email'])
    return jsonify({'message': f"admin {data['username']} created"})



