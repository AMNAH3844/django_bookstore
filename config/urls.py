from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')), 

    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace='store')),  # ✅ Namespace is required here
]

