from App.models import User, User_Competition
#Competition,User, 
from App.database import db

def create_competition_user(username, password, email): 
    newUser = User_Competition(username=username, password=password, email=email)

    try:
        db.session.add(newUser)
        db.session.commit()
        return newUser
    
    except:
        return None

def get_competition_user(id):
    return User_Competition.query.get(id)

def update_competition_user(id, username):
    user = get_competition_user(id)

    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

# def findCompUser(user_id, comp_id):
#    user = User_Competition.query.get(user_id)
#    if user:
#        comp = user.query.get(comp_id)
#        if comp:
#            print("yay")
#            return True    
#    print("no bueno")
#    return False