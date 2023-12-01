from App.database import db
from .user import User

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_compID = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(120), nullable=False)
    Ranking = db.Column(db.Integer, db.ForeignKey('ranking.rank'), nullable=True)

    def __init__(self, user_compID, name, Ranking):
        self.user_compID = user_compID
        self.name = name
        self.Ranking = Ranking

    def __repr__(self):
        return f'<Profile name: {self.name} Ranking: {self.Ranking}>'

    def toJSON(self):
        return {
            'User ID': self.user_compID,
            'Name': self.name,
            'Ranking': self.Ranking
        }
    