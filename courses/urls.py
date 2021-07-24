from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyCourseList.as_view(), name="mycourse_list"),
    path("<int:mycourse_id>/", views.MyCourseDetail.as_view()),
    path("sites/", views.SiteList.as_view(), name="site_list"),
]
