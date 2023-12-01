from App.models import Admin
from App.database import db

def create_admin(username, password, email):
    newAdmin = Admin(username=username, password=password, email=email)
    try:
        db.session.add(newAdmin)
        db.session.commit()
        return newAdmin
   
    except:
        return None

def get_admin_by_username(username):
    return Admin.query.filter_by(username=username).first()

def get_admin(id):
    return Admin.query.get(id)

def get_all_admins():
    return Admin.query.all()

def get_all_admins_json():
    admins = Admin.query.all()
    if not admins:
        return []
    admins = [admin.get_json() for admin in admins]
    return admins

def update_admin(id, username):
    admin = get_admin(id)
    if admin:
        admin.username = username
        db.session.add(admin)
        return db.session.commit()
    return None