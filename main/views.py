from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Главаная страница магазина - Home',
        'is_authenticated': True
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('About page')