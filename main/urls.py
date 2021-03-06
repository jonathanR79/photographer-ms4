from django.contrib import admin
from django.urls import path, include
from pages.views import index


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("accounts/", include("accounts.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("pages/", include("pages.urls")),
    path("services/", include("proServices.urls")),
]
