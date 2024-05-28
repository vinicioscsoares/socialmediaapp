from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
rooms = [
    {'id': 1, 'name': 'vamos aprender python'},
    {'id': 2, 'name': 'Aprenda C++'},
    {'id': 3, 'name': 'Aprenda JavaScript'},
]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    return render(request, 'base/room.html')
