from django.urls import path, include, re_path
from . import views as userViews

urlpatterns = [
    path("logout/", userViews._logout, name="logout"),
    path("profile/", userViews.profile, name="profile"),
    path("login-success/", userViews.login_success, name="login-success"),
    re_path(r"^(?P<state>[a-zA-Z])?", userViews.account, name="account"),
    re_path(r"^.*$", userViews.spechul, name="spechul"),
]
