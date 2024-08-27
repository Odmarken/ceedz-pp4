from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('likes/', include('likes.urls')),
    path('', blog_views.post_list, name='home'),  
    path('accounts/', include('django.contrib.auth.urls')),  # Includes login, logout, etc.
]
