from django.http import HttpResponseNotFound
from django.shortcuts import render


def main(request):
    return render(request, 'creative_task/about_me.html')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
