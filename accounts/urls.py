from django.urls import path

from rest_auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
    UserDetailsView,
)
from rest_auth.registration.views import RegisterView

from .views import UserCheck, LoginView, LogoutView

urlpatterns = [
    path(
        "api/password/reset/", PasswordResetView.as_view(), name="rest_password_reset"
    ),
    path(
        "api/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="rest_password_reset_confirm",
    ),
    path("api/login/", LoginView.as_view(), name="rest_login"),
    path("api/logout/", LogoutView.as_view(), name="rest_logout"),
    path(
        "api/password/change/",
        PasswordChangeView.as_view(),
        name="rest_password_change",
    ),
    path("api/registration/", RegisterView.as_view(), name="rest_register"),
    path("api/user/", UserDetailsView.as_view(), name="rest_user_details"),
]

urlpatterns += [
    path("check/<str:email>/", UserCheck.as_view()),
]
