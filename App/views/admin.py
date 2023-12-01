from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    create_admin,
    jwt_required
)

admin_views = Blueprint('admin_views', __name__, template_folder='../templates')

@admin_views.route('/api/admin', methods=['POST'])
def create_admin_action():
    data = request.json
    create_admin(data['username'], data['password'], data['email'])
    return jsonify({'message': f"admin {data['username']} created"}), 201



