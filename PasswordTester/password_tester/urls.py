from django.urls import path
from .views import PasswordTesterView, home

urlpatterns = [
    path('', home, name='home'),
    path('api/test-password/', PasswordTesterView.as_view(), name='test-password'),
]