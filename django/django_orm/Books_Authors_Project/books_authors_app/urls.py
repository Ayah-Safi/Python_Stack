from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addbook', views.addBook),
    path('displaybook/<int:book_id>/', views.displayBook, name='displayBook'),
    path('displaybook/<int:book_id>/addAuthor', views.addAuthor, name='addAuthor'),
    path('author', views.author, name='author'),
    path('addauthor', views.addAuthortoTemplate),
    path('displayauthor/<int:author_id>/', views.displayAuthor, name='displayAuthor'),
    path('displayauthor/<int:author_id>/addBooktoAuthor', views.addBooktoAuthor, name='addBooktoAuthor'),
]