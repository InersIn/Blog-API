from django.urls import path

from .views import index, addPost, updatePost, viewPost, viewUserPost, deletePost

urlpatterns = [
    path('', index.as_view()),
    path('create', addPost.as_view()),
    path('update', updatePost.as_view()),
    path('view/', viewPost),
    path('view/<str:user>', viewUserPost),
    path('delete', deletePost.as_view()),
]
