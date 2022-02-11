from django.contrib import admin
from django.urls import path, include
from client_ip.views import save_ip

urlpatterns = [
    path('', save_ip),
    path('admin/', admin.site.urls),
]
