from django.urls import path
from . import views

urlpatterns = [
    path('v1/', views.main),
    path('checkout/', views.checkout, name='checkout'), 
    path('pay/', views.pay, name='pay'), 
]