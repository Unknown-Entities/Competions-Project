from App.database import db
from .user import User
from .ranking import Ranking

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    rank = db.Column(db.Integer, db.ForeignKey('ranking.id'))
    message = db.Column(db.String, nullable=False)
    read = db.Column(db.Boolean, default=False)
    

    def __init__(self, userId, message, rank):
        self.userId = userId
        self.rank = rank
        self.message = message
        self.read = False

    def get_json(self):
        return {
            'Message ID': self.id,
            'User ID': self.userId,
            'Message': self.message,
            'Rank': self.rank,
            'Read': self.read
        }