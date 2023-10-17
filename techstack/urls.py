from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('auth.api.urls')),
    path('api/v1/product/', include('product.api.urls')),
]
