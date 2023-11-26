from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money',views.earn_gold),
    path('clearsession',views.clear_session)
]