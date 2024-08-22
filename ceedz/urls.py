from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('likes/', include('likes.urls')),
    path('', include('blog.urls')),  
]
