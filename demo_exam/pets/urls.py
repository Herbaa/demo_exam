from django.urls import path
from . import views
app_name = 'pets'

urlpatterns = [
    path('pets/', views.pet_list, name='pet_list'),
    path('create_service/', views.create_service, name='create_service'),
]