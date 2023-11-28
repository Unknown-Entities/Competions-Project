from App.models import Competition,User, User_Competition
from App.database import db

def findCompUser(user_id, comp_id):
    user = User_Competition.query.get(user_id)

    if user:
        comp = user.query.get(comp_id)
        if comp:
            print("yay")
            return True
    
    print("no bueno")
    return False