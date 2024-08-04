from django.urls import path

from . import views


urlpatterns = [
    path('', views.loads, name="loads"),
    path('page2/', views.page2, name="page2"),
]