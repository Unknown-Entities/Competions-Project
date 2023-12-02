import os, tempfile, pytest, logging, unittest
from unittest.mock import patch
from werkzeug.security import check_password_hash, generate_password_hash

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
    create_competition,
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
        user = User("bob", "bobpass", "bob@gmail.com")
        assert user.username == "bob"
        assert user.email == "bob@gmail.com"

    # Pure function no side effects or integrations called  
    def test_get_json(self):
        user = User("bob", "bobpass", "bob@gmail.com")
        user_json = user.get_json()
        self.assertDictEqual(user_json, {"id":None, "username":"bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password, "bob@gmail.com")
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password, "bob@gmail.com")
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
        self.assertDictEqual(admin_json, {"id":None, "username":"jake"})
    
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

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "rickpass", "rick@gmail.com")
        assert user.username == "rick"

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

    def test_add_user_to_comp(self):
        newcomp = create_competition("Walktime", "Port of Spain")
        if newcomp:
            assert add_user_to_comp(1, 1, 4)
        else:
            assert False

    def test_get_user_competitions(self):
        comp = get_user_competitions(1)
        user_competitions = []

        for usercomp in comp:
            del usercomp["date"]
            del usercomp["participants"]
            user_competitions.append(usercomp)
        
        expected_list = [{"id": 1, "name": "Walktime", "location": "Port of Spain"}]
        self.assertListEqual(expected_list, user_competitions)


    def test_get_user_rankings(self):
        users = get_user_rankings(1)
        
        self.assertListEqual([{"id":1, "comp_id": 1 , "user_id": 1, "rank": 4}], users)
    
    def test_update_admin(self):
        update_admin(1, "freeport")
        user = get_admin(1)
        assert user.username == "freeport"

    def test_admin_add_comp(self):
        user = create_admin("maraval", "maravalpass", "maraval@gmail.com")
        comp = user.add_comp("walktime", "2 dabloons", "NA", 21)
        self.assertIsNotNone(comp, "")
   
    def test_send_notification_success(self):
        notifi_service = notify("1", "The top 20 rankings have changed")
        user_id = get_all_users_json()
        message = "Success !! These are the new rankings!"

        with patch('App.models.Notification.notify') as mock_notification:
            result = notifi_service.notify(user_id, message)

        mock_notification.assert_called_once_with(user_id, message)
        self.assertTrue(result)

    def test_send_notification_failure(self):
        notifi_service = notify("1", "The top 20 rankings have changed")
        user_id = get_all_users_json()
        message = "Failed to send notification."

        # Act
        with patch('App.models.Notification.notify') as mock_notification:
            mock_notification.side_effect = Exception("Notification was unsucessfull in notifying uers of rank change")
            result = notifi_service.notify(user_id, message)

        # Assert
        mock_notification.assert_called_once_with(user_id, message)
        self.assertFalse(result)
