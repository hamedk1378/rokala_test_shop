from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view(), name='rest_register'),
]