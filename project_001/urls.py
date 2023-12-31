from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from project_001 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_001.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
