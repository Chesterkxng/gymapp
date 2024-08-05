from django.urls import path
from session import views

urlpatterns = [
    path('sessions/', views.sessions, name="sessions"),
    path('session/add', views.addSession, name='session/add'),
    path('session/update', views.updateSession, name='session/update'),
    path('session/reconduct', views.reconductSession, name='session/reconduct'),
    path('session/delete', views.deleteSession, name='session/delete')
]
