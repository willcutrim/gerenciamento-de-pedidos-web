from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from produtos.viewset import ProdutosViewSet

router = routers.DefaultRouter()
router.register('produtos', ProdutosViewSet)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    path('admin/', admin.site.urls),

    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),


    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),

    path('usuario/', include('usuario.urls')),


    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
