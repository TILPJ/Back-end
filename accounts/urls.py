from django.urls import path

from rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from rest_auth.registration.views import RegisterView

urlpatterns = [
    path("api/login/", LoginView.as_view(), name="api_login"),
    path("api/logout/", LogoutView.as_view(), name="api_logout"),
    path(
        "api/password/change/", PasswordChangeView.as_view(), name="api_password_change"
    ),
    path("api/registration/", RegisterView.as_view(), name="api_register"),
]
