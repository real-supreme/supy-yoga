from django.urls import path, include, re_path
from . import views as batchViews

urlpatterns = [
    path("", batchViews.enroll, name="enroll"),
    path("accounts/", batchViews.account, name="be-account"),
]
