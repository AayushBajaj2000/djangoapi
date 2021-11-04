import json

from rest_framework.parsers import JSONParser
from .models import State
from .serializers import StateSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
import requests

@csrf_exempt
def state(request):
    if request.method == 'GET':
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        unicode = request.body.decode('utf-8')
        data = {"light_1": unicode[6:]}
        serializer = StateSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return redirect("/")
        return JsonResponse(serializer.errors, status=400)

def home(request):
    x = requests.get('http://localhost:8000/state/')
    data = x.json()
    currentState = data[-1]['light_1'] # Get the latest data
    return render(request, "app.html", {'currentState': currentState})
