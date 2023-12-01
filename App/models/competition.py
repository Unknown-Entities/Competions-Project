from datetime import datetime
from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    date = db.Column(db.DateTime, default= datetime.utcnow)
    # rank = db.Column(db.Integer)
    location = db.Column(db.String(120), nullable=False)

    participants = db.relationship("User_Competition", lazy=True, backref=db.backref("users"), cascade="all, delete-orphan")


    def __init__(self, name, location):
        self.name = name
        self.location = location


    
    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'location': self.location
        }



    def toDict(self):
        res = {
            "ID": self.id,
            "Name": self.name,
            "Date": self.date,
            "Location": self.location,
            "Participants": [participant.toJSON() for participant in self.participants]
        } 
        return res
