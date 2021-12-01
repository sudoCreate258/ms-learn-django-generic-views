from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', views.shelter_list, name='shelter_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),

    # TODO: Register detail view
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),

    # TODO: Register create view


]
