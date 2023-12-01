from .user import User
from App.database import db 

class User_Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __init__(self, profile, comp_id, rank):
        self.profile = profile
        self.comp_id = comp_id
        self.rank = rank
    
    def toJSON(self):
        return{
            'Profile ID': self.profile,
            'Competition ID': self.comp_id,
            'Rank': self.rank
        }