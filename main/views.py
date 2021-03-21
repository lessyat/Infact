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
    print(facts)
    return render(request, 'main/game.html')
