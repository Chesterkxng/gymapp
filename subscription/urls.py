from django.urls import path
from subscription import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', views.subscriptions, name='subscriptions'), 
    path('subscription/add', views.addSubscription, name='subscription/add'),
    path('subscription/update', views.updateSubscription, name='subscription/update'),
    path('subscription/reconduct', views.reconductSubscription, name='subscription/reconduct'),
    path('subscription/delete', views.deleteSubscription, name='subscription/delete')
]
