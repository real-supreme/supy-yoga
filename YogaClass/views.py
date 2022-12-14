from django.shortcuts import render
from asgiref.sync import sync_to_async


@sync_to_async
def index(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def error_404_view(request, exception):
    print(exception)
    return render(request, "404.html")
