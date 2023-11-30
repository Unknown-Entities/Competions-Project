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

def get_user_competitions(user_id):
    user = User.query.get(user_id)    
    if user:
        userComps = user.competitions
        competitions = [Competition.query.get(inst.comp_id) for inst in userComps]
        print(competitions)
        if competitions:
            results =  [c.toDict() for c in competitions] 
            return results
        else:
            return competitions
    return ("User not Found")

def add_user_to_comp(user_id, comp_id, rank):
    user = User.query.get(user_id)
    comp = Competition.query.get(comp_id)
    user_comp = User_Competition.query.filter_by(user_id=user.id, comp_id=comp.id).first()
    if user_comp:
        return False        
    if user and comp:
        user_comp = User_Competition(user_id=user.id, comp_id=comp.id, rank = rank)
        try:
            db.session.add(user_comp)
            db.session.commit()
            return True
        except Exception as e:
            print("FAILURE")
            db.session.rollback()
            return False            
        print("success")
    return 'Error adding user to competition'

def findCompUser(user_id, comp_id):
    user = User_Competition.query.get(user_id)
    if user:
        comp = user.query.get(comp_id)
        if comp:
            print("yay")
            return True    
    print("no bueno")
    return False