from App.models import User, Competition, User_Competition, Profile
from App.database import db

def get_profile(id):
    profile = Profile.query.filter_by(user_compID=id).first()
    return profile

def create_profile(id, username):
    newprofile = Profile(user_compID=id, name=username, Ranking=None)
    try:
        db.session.add(newprofile)
        db.session.commit()
        return newprofile
    except:
        return None