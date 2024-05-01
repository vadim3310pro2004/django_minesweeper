from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .auto_docs import urlpatterns as auto_docs_urlpatterns


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('minesweeper/', include('minesweeper.urls')),
    path('autodocs/', include(auto_docs_urlpatterns)),
]


if settings.DEBUG == True:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
