from App.database import db
from .user import User

class Profile(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_compID = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(120), nullable=False)
    globalRanking = db.Column(db.Integer, db.ForeignKey('ranking.rank'), nullable=False)
 #   university = db.Column(db.String(300), nullable=False)

    def __init__(self, ID, user_compID, name): #university
        self.ID = ID
        self.user_compID = user_compID
        self.name = name
    #    self.university = university

    def __repr__(self):
        return f'<Profile name: {self.name} Global ranking: {self.globalRanking}>'
    #university: {self.university}

    def toJSON(self):
        return {
            'ID': self.ID,
            'user_compID': self.user_compID,
            'name': self.name
          #  'university': self.university
        }
    