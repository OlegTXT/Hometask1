from django.urls import path
from auth_users.views import *

urlpatterns = [
    path('login/', auth_login, name='login'),
    path('logout/', auth_logout, name='logout'),
]
