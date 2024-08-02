from django.urls import path
from subscription import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('addSubscription/', views.addSubscription, name='addSubscription'),
    path('updateSubscription/<int:id>', views.updateSubscription, name='updateSubscription'),
    path('reconductSubscription/<int:id>', views.reconductSubscription, name='reconductSubscription')
]
