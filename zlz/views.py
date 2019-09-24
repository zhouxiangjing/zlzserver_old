from django.shortcuts import render
from django.http import HttpResponse

import os
# Create your views here.


def index(request):
    return render(request, 'zlz/index.html')


def media(request):
    if request.method == "POST":
        my_file = request.FILES.get("file", None)
        if not my_file:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("media", my_file.name), 'wb+')
        for chunk in my_file.chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")



