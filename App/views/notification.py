from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from .index import index_views

from App.controllers import (
    jwt_required,
    notify,
    calculate_ranking,
    get_top_20_users_rank,
    get_all_notifications_json
)

notification_views = Blueprint('notification_views', __name__, template_folder='../templates')

@notification_views.route('/notifications/20', methods=['GET'])
@jwt_required()
def notify_top_ranks():
    if jwt_current_user.user_type == "Admin":
      check = get_top_20_users_rank()
      calculate_ranking()
      if check:
        rank_list = len(check) + 1
        for num in range(1, rank_list):
          message = notify(num, "Your rank has been updated!")
        return jsonify({"message": f"Notifications sent"}), 200
      return jsonify({"error": f"Notifications failed to send"}), 401
    return (jsonify({'error': f"only admins can notify users"}),500)

@notification_views.route('/notifications', methods=['Get'])
@jwt_required()
def get_all_notifications():
  if jwt_current_user.user_type == "Admin":
    notif = get_all_notifications_json()
    return jsonify(notif)
  return (jsonify({'error': f"only admins can check sent notifications"}),500)              