from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),
    path('new', views.new),         
    path('create', views.create),  
    path('<int:id>', views.showTV),
    path('<int:id>/edit', views.edit_show),
    path('update', views.update_show),
    path('delete/<id>', views.delete_show),

]