from django.urls import path
from subscription import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('addSubscription/', views.addSubscription, name='addSubscription'),
    path('updateSubscription/', views.updateSubscription, name='updateSubscription'),
    path('reconductSubscription/', views.reconductSubscription, name='reconductSubscription'),
    path('deleteSubscription/', views.deleteSubscription, name='deleteSubscription')
]
