from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'map/index.html')


def popup(request):
    if request.method == "POST":
        return render(request, 'map/index.html', {"lat": request.POST["lat"], "lng": request.POST["lng"]})
    else:
        return render(request, 'map/popup.html')

