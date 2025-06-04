from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('template/<int:template_id>/create/', views.create_report, name='create_report'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
]
