from django.shortcuts import render, get_object_or_404
from .models import Book, Author

def listar_livros(request):
    books = Book.objects.all()

    return render(request, 'lista_livros.html', {'books': books})


def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    books = author.books.all()

    return render(request, "author_details.html", {
        "author": author,
        "books": books,
    })