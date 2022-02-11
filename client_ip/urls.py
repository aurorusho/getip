from django.urls import path
from . import views


app_name = 'client_ip'


urlpatterns = [
    path('print_test/', views.get_city)
]

