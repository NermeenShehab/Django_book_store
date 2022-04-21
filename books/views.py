from multiprocessing import context
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse
from django.conf import settings
from .forms import BookCreate
from .models import Author, Book

# Create your views here.


def index(request):
    shelf = Book.objects.all()
    return render(request, 'books/library.html', {'shelf': shelf})


def get_book (request,id ):
    book = get_object_or_404(Book , id=id)
   
    context ={
        'book' : book ,
    }
    return render(request,'books/book.html' ,context= context)


def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'books/upload_form.html', {'upload_form': upload})


def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('index')
    return render(request, 'books/upload_form.html', {'upload_form': book_form})


def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')

def authors(request):
    context = {"authors" : Author.objects.all()}
    return render(request,'books/author.html' , context = context)

def author_detail (request,id):
    books = Book.objects.filter(author=id).all()
    context ={
        'p' : books[0].author ,
        'books' : books  ,
    }
    return render(request,'books/author_detail.html' , context)