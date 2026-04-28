from django.urls import path 
from . import views
from .views import post_list, create_post, delete_post

urlpatterns = [
    path('post_list', post_list, name='post_list'),
    path('create', create_post, name='create_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]