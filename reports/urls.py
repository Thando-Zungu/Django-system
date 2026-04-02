from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.submit_report, name='submit_report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
]