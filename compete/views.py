from django.shortcuts import render


def index(request):
    context = {
        "temp": "temp"
    }
    return render(request, 'compete/base.html')
