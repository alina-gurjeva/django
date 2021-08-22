from django.shortcuts import render
import json
from products.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop',
        'h1_heading': 'GeekShop Store',
        'description': 'Новые образы и лучшие бренды на GeekShop Store.\n'
                       'Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'button_text_to_start_shopping': 'Начать покупки'
    }
    return render(request, 'products/index.html', context)


def products(request):

    context = {
        'items': Product.objects.all(),
        'h1_heading': 'GeekShop',
        'title': 'GeekShop - Каталог',
        'groups': ProductCategory.objects.all()
    }

    # [{'name': 'Новинки', 'href': '#'}, {'name': 'Одежда', 'href': '#'},
    #  {'name': 'Обувь', 'href': '#'}, {'name': 'Аксессуары', 'href': '#'},
    #  {'name': 'Подарки', 'href': '#'}]
    return render(request, 'products/products.html', context)
