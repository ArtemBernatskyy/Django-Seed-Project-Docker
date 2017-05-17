from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^', include('testproj.landing.urls', namespace='landing')),
    url(r'^accounts/', include('testproj.accounts.urls', namespace='accounts')),
    url(r'^auth/', include('testproj.registration.backends.default.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
