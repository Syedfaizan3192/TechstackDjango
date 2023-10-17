from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (RegistrationViewSet, LogoutViewSet, CustomAuthToken)

urlpatterns = [
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('register/', RegistrationViewSet, name='register'),
    path('logout/', LogoutViewSet, name='logout'),
]
