from django.urls import path
from .views import registration, post_list, post_detail, post_create, post_edit, post_delete

urlpatterns = [
    path('registration/', registration, name='register'),
    path('', post_list, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', post_create, name='post_create'),
    path('post/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', post_delete, name='post_delete'),
]