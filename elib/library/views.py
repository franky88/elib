from django.shortcuts import render
from .models import User, Book, BooksBorrow, Author, Category
# Create your views here.
def bookList(request):
	book_list=Book.objects.all()
	context={
		"title": "List of books",
		"book_list": book_list,
	}
	return render(request, "library/library_book.html", context)