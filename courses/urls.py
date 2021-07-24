from django.urls import path

from . import views

urlpatterns = [
    path("", views.MyCourseList.as_view(), name="mycourses_list"),
    path("<int:mycourse_id>/", views.MyCourseDetail.as_view()),
]
