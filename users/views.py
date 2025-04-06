from django.shortcuts import render

def login(request):
    context = {
        'title': 'Поршень - Авторизация'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Поршень - Регистрация'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Поршень - Кабинет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...