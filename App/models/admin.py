from .user import User
from App.database import db 

class Admin(User):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.user_type = "admin"
        self.email = email


    def __repr__(self):
        return f'<Admin {self.id} {self.username} {self.email}>'
    
    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'type': 'admin',
            'email': self.email
        }