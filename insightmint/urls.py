from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('reports/new/', views.report_create, name='report_create'),
    path('reports/<int:pk>/', views.report_detail, name='report_detail'),
]
