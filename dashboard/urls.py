from django.urls import path
from dashboard import views

urlpatterns = [
    path('dashboard/subscriptions', views.subscriptions, name="dashboard/subscriptions"), 
    path('dashboard/sessions', views.sessions, name="dashboard/sessions")
]
