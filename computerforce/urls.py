from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # core namespace
    path("", include(("core.urls", "core"), namespace="core")),

    # accounts namespace (si la tienes)
    path("accounts/", include(("accounts.urls", "accounts"), namespace="accounts")),
]
