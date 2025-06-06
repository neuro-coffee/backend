from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='swagger-ui')),
    path('admin/', admin.site.urls),
]

swagger_urls = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

api_urls = [
    path('api/products/', include('apps.products.urls', namespace='products')),
    path('api/users/', include('apps.users.urls', namespace='users')),
]

urlpatterns += swagger_urls
urlpatterns += api_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
