from App.models import User, Competition, User_Competition
from App.database import db

def create_user(username, password, email):
    newuser = User(username=username, user_type="Competitor", password=password, email=email)
    try:
        db.session.add(newuser)
        db.session.commit()
        return newuser
    except:
        return None

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def obtain_user_profile(ID):
    User_profile = User.query.get(ID)

    if User_profile:
        return User_profile.toJSON()

    return f'{ID} This user`s profile ID cannot be not found'

#def get_ranked_users():
#    return User.query.order_by(User.rank.asc()).all()

# def update_ranks():
#   users = User.query.order_by(User.rank.asc()).limit(20).all()
  
#   # Store current ranks
#   ranks = {u.id: u.rank for u in users}
  
#   # Update ranks
#   db.session.query(User).update({User.rank: User.rank + 1})  
#   db.session.commit()

#   # Check if ranks changed
#   for u in users:
#     if u.rank != ranks[u.id]:
#       send_notification(u, f"Your rank changed from {ranks[u.id]} to {u.rank}")
    