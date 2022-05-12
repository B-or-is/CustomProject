"""
Такой способ создания пользовательской страницы ошибки 404 “Страница не найдена”
предлагается официальной документацией Django (views.py - в каталоге проекта, а не приложения)
"""

from django.shortcuts import render


def page_not_found_view(request, exception):
    # return render(request, '404.html', status=404)
    return render(request, 'index.html')
