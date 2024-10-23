from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("web.urls")),  # URL raíz que apunta a la app "web"
]
