from django.urls import re_path
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_bulk.routes import BulkRouter

urlpatterns = [
    re_path('^user/login$', obtain_jwt_token),
    # re_path('^user/login$', views.TestView.as_view()),
    re_path(r'^api-token-refresh/$', refresh_jwt_token),
    re_path(r'^api-token-verify/$', verify_jwt_token),
    re_path(r'^user/info$', views.UserView.as_view()),
    re_path(r'^user/logout$', views.UserView.as_view()),
]

router = BulkRouter()
router.register(r'roles', views.GroupView)
router.register(r'server', views.ServerView)
router.register(r'users', views.UsersView)
urlpatterns += router.urls
