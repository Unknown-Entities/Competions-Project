from App.database import db
from .user import User

class Profile(db.Model):
    profileID = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, db.ForeignKey(User.id))
    name = db.Column(db.String(120), nullable=False)
    university = db.Column(db.String(300), nullable=False)
    globalRanking = db.relationship('Ranking', backref=db.backref('competition', lazy='joined'))

    def __init__(self, profileID, studentID, name, university):
        self.profileID = profileID
        self.studentID = studentID
        self.name = name
        self.university = university

    def __repr__(self):
        return f'<Profile name: {self.name} university: {self.university} Global ranking: {self.globalRanking}>'

    def toJSON(self):
        return {
            'profileID': self.profileID,
            'studentID': self.studentID,
            'name': self.name,
            'university': self.university
        }