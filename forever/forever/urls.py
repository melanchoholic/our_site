from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('we/', include('we.urls')),
    path('gnel/', include('gnel.urls')),
    path('nastya/', include('nastya.urls')),
    #  path('secret/', include('secret.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

handler404 = 'core.views.page_not_found'
