from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    jwt_required,
    create_competition,
    get_all_competitions_json,
    get_competition_by_id,
    get_user_rankings,
    add_user_to_comp
)


comp_views = Blueprint('comp_views', __name__, template_folder='../templates')


##return the json list of competitions fetched from the db
@comp_views.route('/competitions', methods=['GET'])
@jwt_required()
def get_competitons():
    competitions = get_all_competitions_json()
    return (jsonify(competitions),200) 

##add new competition to the db
@comp_views.route('/competitions', methods=['POST'])
@jwt_required()
def add_new_comp():
    if jwt_current_user.user_type == "Admin":
        data = request.json
        response = create_competition(data['name'], data['location'])
        if response:
            return (jsonify({'message': f"competition created"}), 201)
        return (jsonify({'error': f"error creating competition"}),500)
    return (jsonify({'error': f"only admins can create competitions"}),500)

@comp_views.route('/competitions/<int:id>', methods=['GET'])
@jwt_required()
def get_competition(id):
    print(id)
    competition = get_competition_by_id(id)
    if not competition:
        return jsonify({'error': 'competition not found'}), 404 
    return (jsonify(competition.toDict()),200)

@comp_views.route('/competitions/results', methods=['POST'])
@jwt_required()
def add_comp_results():
    if jwt_current_user.user_type == "Admin":
        data = request.json
        response = add_user_to_comp(data['user_id'],data['comp_id'], data['rank'])
        if response:
            return (jsonify({'message': f"results added successfully"}),201)
        return (jsonify({'error': f"error adding results"}),500)
    return (jsonify({'error': f"only admins can add results"}),500)




