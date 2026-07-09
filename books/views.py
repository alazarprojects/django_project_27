from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from .forms import BookForm


# Create your views here.

# functions that manage our web pages.

def home(request: HttpRequest):
    return HttpResponse("Hello from our books app!")

# functions-based view:
# CRUD: Create, Read, Update, Delete.

def create_book(request: HttpRequest):
    if request.method == "POST":
        #dateliile book-ului care au fost trimise de form folosind HTTP POST request, se afla in request.POST ca un dictionar.
        book_instance = BookForm(request.POST)
        if book_instance.is_valid():
            # aici se creeaza un book in baza de date!
            book_instance.save()
            return redirect("create_book")
    else:
        #in cazul asta, requestul poate fi GET, PUT, PATCH, DELETE, etc..
        form = BookForm()
        list1 = [10, 20, 30 ,40]
        return render(request, "books/book_form.html", context={"form": form, "list1": list1})

