from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response

from .models import *
from .serializers import *
import random
import requests


def dashboard_view(request):
    return render(request, 'main/dashboard.html')


def categories_view(request):
    return render(request, 'main/categories.html')


def game_view(request, category_id):
    facts = Fact.objects.filter(category=category_id)
    fact = random.choice(facts)
    context = {"fact": fact}
    return render(request, 'main/game.html', context=context)


def like_view(request, phrase_id):
    if request.GET.get('like-btn'):
        fact = Fact.objects.get(phrase=phrase_id)
        fact.popularity += 1
    return render(request, 'main/game.html')