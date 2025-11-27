from django.contrib import admin
from django.urls import path, include
from academy import urls
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('academy/', include('academy.urls')),  
    path('',views.Home,name='home'),
    path('accounts/',include('accounts.urls')) 
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
