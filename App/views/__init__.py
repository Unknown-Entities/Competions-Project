# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .competition import comp_views
from .notification import notification_views
from .admin import admin_views
from .profile import profile_views
from .user_competition import user_competition_views
from .ranking import rank_views


views = [user_views, index_views, auth_views, comp_views, notification_views, admin_views, profile_views, user_competition_views, rank_views] 
# blueprints must be added to this list