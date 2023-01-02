from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from bucsani_school import settings
from bucsani_school.views import PostAPI, GalleryAPI, DocumentsAPI, SiteConfigAPI, PostTypeAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls')),

    path("users/", include("users.urls")),

    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="index"),
]

# DRF router
router = routers.DefaultRouter()
router.register(r"post", PostAPI)
router.register(r"post-types", PostTypeAPI)
router.register(r"gallery", GalleryAPI)
router.register(r"config", SiteConfigAPI)
router.register(r"document", DocumentsAPI)


urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
