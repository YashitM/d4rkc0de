from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        "temp": "temp"
    }
    return render(request, 'practice/index.html', context)
