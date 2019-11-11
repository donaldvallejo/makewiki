from django.contrib import admin
from wiki import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wiki.urls')),
]
