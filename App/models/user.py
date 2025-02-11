from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    user_type = db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    competitions = db.relationship("User_Competition", lazy=True, backref=db.backref("user"), cascade="all, delete-orphan")
    profiles = db.relationship("Profile", lazy=True, backref=db.backref("user"), cascade="all, delete-orphan")
    admins = db.relationship("Admin", lazy=True, backref=db.backref("user"), cascade="all, delete-orphan")
    notifications = db.relationship("Notification", lazy=True, backref=db.backref("user"), cascade="all, delete-orphan")

    def __init__(self, username, user_type, password, email):
        self.username = username
        self.user_type = user_type
        self.email = email
        self.set_password(password)        

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'user_type': self.user_type,
            'email': self.email
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<User {self.id} {self.username} {self.email}'
    