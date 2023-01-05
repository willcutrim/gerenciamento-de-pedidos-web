from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from produtos.viewset import ProdutosViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),


    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
