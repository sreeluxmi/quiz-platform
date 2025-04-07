from django.urls import path

#local
from .apis.auth import RegistrationView



urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
]