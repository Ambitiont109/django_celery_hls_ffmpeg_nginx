from django.urls import path

from .views import StartStreamView, StopStreamView

app_name = "stream_m3u8"
urlpatterns = [
    path("", StartStreamView.as_view(), name="start_stream"),
    path("stop/", StopStreamView.as_view(), name="stop_stream")
]
