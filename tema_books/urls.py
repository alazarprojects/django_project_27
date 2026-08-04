from django.urls import path
from . import views

urlpatterns = [
    path("data/ordered_names", views.list_names),
    path("data/ordered_numbers", views.list_numbers),
    path("data/paired_names", views.list_paired_names),
]
