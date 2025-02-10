from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from wagtail import urls as wagtail_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls

from cheeseapi.search import views as search_views

from .api import api_router

# Redirection vers admin en production
def redirect_to_admin(request):
    return redirect('admin/')

# URLs de base communes
urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path("search/", search_views.search, name="search"),
    path('api/v2/', api_router.urls),
]

# En développement, on garde toutes les URLs
if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    # Ajoute les URLs Wagtail en développement
    urlpatterns += [
        path("", include(wagtail_urls)),
    ]
else:
    # En production, redirige la racine vers l'admin
    urlpatterns = [path('', redirect_to_admin)] + urlpatterns
