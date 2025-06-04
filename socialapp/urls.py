from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:username>/', views.profile_detail, name='profile_detail'),
]
