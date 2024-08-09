from django.urls import path

from . import views


urlpatterns = [
    path('student/check/', views.CheckCreateStudent.as_view(), name="check_create_student"),
]