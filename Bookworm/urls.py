
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('' , include('ImageComp.urls')),
    path('admin/', admin.site.urls),
    
]
