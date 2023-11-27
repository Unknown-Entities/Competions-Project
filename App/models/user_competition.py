from .user import User
from App.database import db 

class User_Competition(User):
    __tablename__ = 'user_competition'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    profile = db.relationship('Profile', backref=db.backref('user_competition', lazy='joined'))
    competition = db.relationship('Competition', backref=db.backref('competitor', lazy='joined'))

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.user_type = "user_competition"
        self.email = email


    def __repr__(self):
        return f'<user_competition {self.id} {self.username} {self.email}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': 'user_competition',
            'email': self.email
        }