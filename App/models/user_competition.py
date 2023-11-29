from .user import User
from App.database import db 

class User_Competition(User):
    __tablename__ = 'user_competition'
    id = db.Column(db.Integer, db.ForeignKey(User.id), primary_key=True)
    profile = db.Column(db.Integer, db.ForeignKey('profile.ID'), nullable=False)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)

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