from django.contrib import admin
from django.urls import path, include

from accounts import views

urlpatterns = [
    path("", views.api_root),
    path("admin/", admin.site.urls),
    path("v1.0/accounts/", include("accounts.urls")),
]
