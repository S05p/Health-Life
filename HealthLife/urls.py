from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import settings

urlpatterns = [
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('',include('articles.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
