from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API
    path('api/v1/', include('api.urls')),
]
