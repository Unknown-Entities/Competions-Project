import os, tempfile, pytest, logging, unittest
from unittest.mock import patch
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify

from App.main import create_app
from App.database import db, create_db
from App.models import User, User_Competition, Admin, Notification, Ranking, Profile, Competition 
from App.controllers import (
    create_user,
    create_admin,
    get_all_users_json,
    login,
    get_user,
    get_admin,
    get_user_by_username,
    update_user,
    update_admin,
    get_user_competitions,
    get_competition_by_id,
    get_all_competitions_json,
    get_rankings,
    get_rankings_json,
    create_competition,
    create_ranking,
    add_user_to_comp,
    get_user_rankings,
    generate_notification,
    notify,
    get_all_notifications,
    get_all_notifications_json
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):
    
    # Test for average base user
    def test_new_user(self):
        user = User("bob", "Competitor", "bobpass", "bob@gmail.com")
        assert user.username == "bob"
        assert user.email == "bob@gmail.com"

    # Pure function no side effects or integrations called  
    def test_get_json(self):
        user = User("bob", "Competitor", "bobpass", "bob@gmail.com")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"email":"bob@gmail.com", "id":None, "user_type":"Competitor", "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", "Competitor", password, "bob@gmail.com")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", "Competitor", password, "bob@gmail.com")
        assert user.check_password(password)

    # Test for new admin user
    def test_new_admin_user(self):
        admin = Admin("jake", "jakepass1", "jake@gmail.com")
        assert admin.username == "jake"
        assert admin.email == "jake@gmail.com"

    # pure function no side effects or integrations called
    def test_get_admin_json(self):
        admin = Admin("jake", "jakepass1", "jake@gmail.com")
        admin_json = admin.get_json()
        self.assertDictEqual(admin_json, {"email":"jake@gmail.com", "id":None, "user_type":"Admin", "username":"jake"})
    
    def test_admin_hashed_password(self):
        password = "myadminpass"
        hashed = generate_password_hash(password, method='sha256')
        admin = Admin("jake", password, "jake@gmail.com")
        assert admin.password != password

    def test_check_admin_password(self):
        password = "myadminpass"
        admin = Admin("jake", password, "jake@gmail.com")
        assert admin.check_password(password)

'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


def test_authenticate():
    user = create_user("bob", "bobpass", "bob@gmail.com")
    assert login("bob", "bobpass") != None

class UserIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "rickpass", "rick@gmail.com")
        assert user.username == "rick"

    def test_create_admin(self):
        admin = create_admin("maraval", "maravalpass", "maraval@gmail.com")
        assert admin.username == "maraval"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"email":"maraval@gmail.com", "id": 1, "user_type":"Admin", "username":"maraval"}, {"email":"rick@gmail.com", "id": 2, "user_type":"Competitor", "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"
        
    def test_get_competitions(self):
        newcomp = create_competition("Walktime", "Port of Spain")
        comp = get_all_competitions_json()
        user_competitions = []

        for usercomp in comp:
            del usercomp["Date"]
            del usercomp["Participants"]
            user_competitions.append(usercomp)
        
        expected_list = [{"ID": 1, "Location": "Port of Spain", "Name": "Walktime"}]
        self.assertListEqual(expected_list, user_competitions)
    
    def test_update_admin(self):
        update_admin(1, "freeport")
        user = get_admin(1)
        assert user.username == "freeport"
''' 
    def test_send_notification(self):
        notifi_service = notify(1, "The top 20 rankings have changed")
        user_id = get_all_users_json()
        message = "Success !! These are the new rankings!"

        with patch('App.controllers.Notification.notify') as mock_notification:
            result = notifi_service.notify(user_id, message)

        mock_notification.assert_called_once_with(user_id, message)
        self.assertTrue(result)
'''