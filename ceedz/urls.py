from django.contrib import admin
from django.urls import path, include
from blog.views import post_list  
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500, handler403, handler400
from . import views 

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

# Media section
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Error handlers
handler404 = 'ceedz.views.custom_404'
handler500 = 'ceedz.views.custom_500'
handler403 = 'ceedz.views.custom_403'
handler400 = 'ceedz.views.custom_400'
