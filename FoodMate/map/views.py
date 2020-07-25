from django.shortcuts import render

# Create your views here.

def popup(request):
    return render(request, 'map/popup.html')