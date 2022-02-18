from django.shortcuts import render, redirect
from django.views import View
from .tasks import stream_task, test_task
# Create your views here.
is_live = False
url_list = []
task = None

class StartStreamView(View):
    def get(self, request):
        global is_live
        if task is None:
            is_live = False
        elif task.state == "PROGRESS" or task.state == "STARTED":
            is_live = True
        else:
            is_live = False
        if task is not None:
            print(task.state)
        context = {
            "is_live": is_live,
            "url_list": url_list
        }
        return render(request, "stream_m3u8/start_stream.html", context)

    def post(self, request):
        global url_list, task_id, task
        print(request.POST)
        url_list = [
            request.POST.get("url1", ""),
            request.POST.get("url2", ""),
            request.POST.get("url3", "")
        ]
        task = stream_task.delay(url_list)
        print(task.id)
        return redirect('stream_m3u8:start_stream')


class StopStreamView(View):
    def post(self, request):
        global task
        task.revoke(terminate=True)
        return redirect('stream_m3u8:start_stream')
    # def post(self, request):
