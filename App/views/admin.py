from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    # create_user,
    # jwt_authenticate, 
    # get_all_users,
    # get_all_users_json,
    jwt_required,
    create_competition,
    get_all_competitions_json,
    get_competition_by_id,
    add_results,
    get_user_rankings,
    add_user_to_comp
)

admin_views = Blueprint('notification_views', __name__, template_folder='../templates')

@admin_views.route('/users', methods=['POST'])
def create_admin():
    data = request.form
    flash(f"User {data['username']} created!")
    #create_admin(data['username'], data['password'])
    newAdmin = Admin(create_user(data['username'], data['password']))
    return newAdmin

@admin_views.route('/users', methods=['GET'])
def get_admin_by_username():
    return Admin.query.filter_by(username=username).first()

@admin_views.route('/users', methods=['GET'])
def get_admin():
    return Admin.query.get(id)

@admin_views.route('/users', methods=['GET'])
def get_all_admins():
    return Admin.query.all()

@admin_views.route('/users', methods=['GET'])
def get_all_admins_json():
    admins = Admin.query.all()
    if not admins:
        return []
    admins = [admin.get_json() for admin in admins]
    return admins

@admin_views.route('/users', methods=['GET'])
def update_admin():
    admin = get_admin(id)
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None



