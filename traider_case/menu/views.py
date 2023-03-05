from django.shortcuts import render


def index(request):
    url = request.path
    return render(request, 'index.html', {'url': url})
