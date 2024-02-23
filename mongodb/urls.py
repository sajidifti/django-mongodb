from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("add/", views.add_person, name="add"),
    path("all/", views.get_all_persons, name="all"),
]
