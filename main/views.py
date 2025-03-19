from sre_parse import CATEGORIES
from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

def index(request):

    context = {
        'title': 'Поршень - Главная',
        'content' : 'Автосалон Поршень',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Поршень - О нас',
        'content' : 'О нас',
        'text_on_page': "Выберите наш автосалон Поршень — здесь вы найдете надежные автомобили, выгодные условия и профессиональное обслуживание без лишних хлопот!"
    }

    return render(request, 'main/about.html', context)