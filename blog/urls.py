from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
]
handler404 = 'main.handler.HttpError.handler404'
handler403 = 'main.handler.HttpError.handler403'