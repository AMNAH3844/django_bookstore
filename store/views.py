from django.shortcuts import render, get_object_or_404
from .models import Book, Category

def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'store/book_detail.html', {'book': book})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'store/category_list.html', {'categories': categories})

def books_by_category(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    books = Book.objects.filter(category=category)
    return render(request, 'store/books_by_category.html', {
        'category': category,
        'books': books
    })

def auth_view(request):
    return render(request, 'store/auth.html')

def cart_view(request):
    return render(request, 'store/cart.html')

def checkout_view(request):
    return render(request, 'store/checkout.html')



