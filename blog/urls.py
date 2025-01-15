from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# from app import views as slug_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('app.urls')),
    
    # path("category/single-blog/<slug:slug>", slug_view.single_blog, name = 'single_blog'),
    # path("single-blog/<slug:slug>", slug_view.single_blog, name = 'single_blog'),

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
