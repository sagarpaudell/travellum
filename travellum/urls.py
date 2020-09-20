from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('pages.urls')),
    path('blog/', include('blog.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('places/', include('places.urls')),
    path('chat/', include('chat.urls')),
    path('view_profile/', include('travellers.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
