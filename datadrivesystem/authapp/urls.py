from django.urls import path
from .views import UserRegistrationAPI, UserLoginAPI

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('api/register/', csrf_exempt(UserRegistrationAPI.as_view()), name='user-registration-api'),
    path('api/login/', csrf_exempt(UserLoginAPI.as_view()), name='user-login-api'),
    # Add more API URL patterns as needed
]
