from werkzeug.security import check_password_hash, generate_password_hash
from .user import User
from App.database import db
from flask_login import UserMixin

class Ranking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255), nullable=False)
    rank = db.Column(db.Integer, nullable=True)
    points = db.Column(db.Integer, nullable=True)

    Ranking = db.relationship('Profile', backref=db.backref('ranking', lazy='joined'))
    notifications = db.relationship('Notification', backref=db.backref('ranking', lazy='joined'))

    def __init__(self, profile_id, name, rank, points):
        self.profile_id = profile_id
        self.name = name
        self.rank = rank
        self.points = points

    def get_json(self):
        return{
            'ID': self.profile_id,
            'Name': self.name,
            'Rank': self.rank,
            'Points': self.points
        }