from django.contrib import admin
from django.urls import path, include
from blog.views import post_list  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  
    path('accounts/', include('django.contrib.auth.urls')),  
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls')),
    path('likes/', include('likes.urls')),
    path('', post_list, name='home'),  
]
