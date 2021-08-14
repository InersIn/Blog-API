from django.urls import path

from .views import users, generateAPIKEY

urlpatterns = [
    path('users', users.as_view()),
    path('generate-api-key', generateAPIKEY.as_view())
]
