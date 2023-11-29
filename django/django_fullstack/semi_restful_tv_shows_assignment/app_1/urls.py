from django.urls import path
from . import views

urlpatterns = [
    path('', views.shows),


    path('new', views.new),         #render a form to create
    path('create', views.create),   #post request to add new record

    path('<int:id>', views.showTV),

    path('<int:id>/edit', views.edit_show),

    path('Update', views.update_show),

    path('delete/<id>', views.delete_show),

]