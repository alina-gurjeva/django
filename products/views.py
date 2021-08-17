from django.shortcuts import render
import json


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
    with open('products/fixtures/products.json', 'r') as fp:
        items = json.load(fp)
    context = {
        'items': items,
        'title': 'GeekShop - Каталог',
        'groups': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки']
    }
    return render(request, 'products/products.html', context)
