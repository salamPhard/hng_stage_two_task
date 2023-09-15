from django.urls import path

from . import views

urlpatterns = [
    path("", views.PersonOverview, name="home"),
    path("create/", views.create_person, name="create"),
    path("all/", views.view_persons, name="all"),
    path("person/<int:pk>/", views.update_person, name="update"),
    path("person/<int:pk>/delete/", views.delete_person, name="delete")

    ]