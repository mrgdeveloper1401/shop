"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from decouple import config
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from shop.base import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # simplejwt url
    path('jwt-api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # admin urls
    path('admin/', admin.site.urls),
    # app url
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('api/blog/', include('blogs.urls', namespace='blogs')),
]

debug_mode = config("DEBUG", cast=bool, default=True)

if debug_mode:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += debug_toolbar_urls()
