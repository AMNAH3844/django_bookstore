from django.urls import path
from . import views

app_name = 'store'  # ✅ Must be placed ABOVE urlpatterns

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),  # Book detail page
    path('categories/', views.category_list, name='category_list'),  # All categories
    path('category/<str:category_name>/', views.books_by_category, name='books_by_category'),  # Books by category
    path('auth/', views.auth_view, name='auth'),  # Registration/Login
    path('cart/', views.cart_view, name='cart'),  # Shopping cart
    path('checkout/', views.checkout_view, name='checkout'),  # Checkout
]
