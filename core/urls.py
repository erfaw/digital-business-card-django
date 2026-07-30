from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.settings import base as base_setting

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path('accounts/', include('accounts.urls')),
]

if base_setting.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)