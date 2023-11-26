from django.shortcuts import render,redirect
from books_authors_app.models import *

def index(request):
    all_books = Books.objects.all
    dict = {'all_books': all_books}
    return render(request,'index.html',dict)

def addBook(request):
   if request.method == "POST":
    tittle = request.POST['tittle']
    description = request.POST['description']
    Books.objects.create(tittle=tittle,desc=description)
    return redirect('/')
   
def displayBook(request,book_id):   
    book_to_display = Books.objects.get(id = book_id)
    authors_of_a_book = book_to_display.authors.all()
    all_authors = Authors.objects.all()
    authors_to_exclude = [author.id for author in authors_of_a_book]
    remaining_authors = all_authors.exclude(id__in=authors_to_exclude)
    context = {'book_to_display': book_to_display,'authors_of_a_book': authors_of_a_book, 'all_authors': remaining_authors}
    return render(request,'displaybook.html',context)    

def addAuthor(request,book_id):
    if request.method == 'POST' :
        book_to_display = Books.objects.get(id = book_id)
        author_id = request.POST ['add-author']
        author = Authors.objects.get(id=author_id)
        authors_of_a_book = book_to_display.authors.all()
        book_to_display.authors.add(author)
        authors_of_a_book = book_to_display.authors.all()
        all_authors = Authors.objects.all()
        authors_to_exclude = [author.id for author in authors_of_a_book]
        remaining_authors = all_authors.exclude(id__in=authors_to_exclude)
        context = {'book_to_display': book_to_display,'authors_of_a_book': authors_of_a_book, 'all_authors': remaining_authors}
    return render(request,'displaybook.html',context)

def author(request):
    all_authors = Authors.objects.all
    dict = {'all_authors': all_authors}
    return render(request,'author.html',dict)

def addAuthortoTemplate(request):
  if request.method == "POST":
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Authors.objects.create(first_name=first_name,last_name=last_name,notes = notes)
    return redirect('/author')
  

def displayAuthor(request,author_id):
    author_to_display = Authors.objects.get(id = author_id)
    books_of_an_author = author_to_display.books.all()
    all_books = Books.objects.all()
    books_to_exclude = [book.id for book in books_of_an_author]
    remaining_books = all_books.exclude(id__in=books_to_exclude)
    context = {'author_to_display': author_to_display,'books_of_an_author': books_of_an_author, 'all_books': remaining_books}
    return render(request,'displayauthor.html',context)

def addBooktoAuthor(request,author_id):
    if request.method == 'POST' :
        author_to_display = Authors.objects.get(id = author_id)
        book_id = request.POST ['add-book']
        book = Books.objects.get(id = book_id)
        books_of_an_author = author_to_display.books.all()
        author_to_display.books.add(book)
        books_of_an_author = author_to_display.books.all()
        all_books = Books.objects.all()
        books_to_exclude = [book.id for book in books_of_an_author]
        remaining_books = all_books.exclude(id__in=books_to_exclude)
        context = {'author_to_display': author_to_display,'books_of_an_author': books_of_an_author, 'all_books': remaining_books}
    return render(request,'displayauthor.html',context)
