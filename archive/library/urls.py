from django.urls import path
from . import views

urlpatterns = [
    path('collections/', views.collection_list, name='collection_list'),
    path('collections/add/', views.add_collection, name='add_collection'),
    path('collections/delete/<str:pk>/', views.delete_collection, name='delete_collection'),
]