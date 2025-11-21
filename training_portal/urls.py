from django.contrib import admin
from django.urls import path, include
from academy import urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('academy.urls')),  
    path('',views.Home,name='home') 
]
