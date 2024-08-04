from django.shortcuts import render, HttpResponse


def loads(request):
    return render(request, 'main/loading.html')


def page2(request):
    if request.user.is_authenticated:
        return HttpResponse(f"Hi! -> { request.user.username }")
    else:
        return HttpResponse(f"Hi! -> Unknown")