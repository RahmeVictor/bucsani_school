from django.urls import path
from rest_framework import routers
from rest_framework.authtoken import views

from users.views import (
    UserAPI,
    CurrentUserView,
    ChangePasswordView,
    SignupView,
    PermissionView,
    GroupView,
    LogoutView,
)

app_name = "users"

# DRF router
router = routers.DefaultRouter()
router.register(r"user", UserAPI)
router.register(r"signup", SignupView)
router.register(r"group", GroupView)
router.register(r"permission", PermissionView)

urlpatterns = [
    path("current-user/", CurrentUserView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
    path("logout/", LogoutView.as_view()),
    # DRF path
    path("login/", views.obtain_auth_token),
]

urlpatterns += router.urls
