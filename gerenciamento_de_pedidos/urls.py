from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pedidos/', include('pedidos.urls')),
    path('produtos/', include('produtos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
