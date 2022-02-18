from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("contact_form.urls")),
    path("server_demo/", include("stream_m3u8.urls"))
]
