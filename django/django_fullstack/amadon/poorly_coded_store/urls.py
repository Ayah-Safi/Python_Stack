from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout),
    path('amadon/display', views.display),
    path('destory', views.destroySession),
]
