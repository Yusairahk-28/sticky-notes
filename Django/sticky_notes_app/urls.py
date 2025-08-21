from django.urls import path
from . import views

# URL patterns to show routing for the application.
urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('detail/<int:pk>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('update/<int:pk>/', views.note_update, name='note_update'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
]
