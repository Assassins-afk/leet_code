from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile_home, name='user_profile'),
]