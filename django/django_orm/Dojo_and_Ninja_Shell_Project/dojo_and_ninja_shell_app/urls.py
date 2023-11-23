from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('processdojo',views.processDojo),
    path('processninja',views.processNinja),
]