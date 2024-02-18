from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .models import Url
from rest_framework.decorators import api_view
from django.http import JsonResponse
import hashlib

import string
import random

def redirect_original_url(request, short_code):
    try:
        url = Url.objects.get(short_code=short_code)
        return redirect(url.original_url)
    except Url.DoesNotExist:
        return HttpResponseNotFound("Short URL not found")
    

@api_view(['POST'])
def create_short_url(request):
    if 'url' in request.data:
        url = request.data['url']
        # Generate a unique hash for the URL
        characters = string.ascii_letters + string.digits
        hash_value = ''.join(random.choice(characters) for _ in range(6))

        url = Url.objects.create(short_code=hash_value, original_url=url)
        return JsonResponse({'short_url': f'/url/{hash_value}/'}, status=201)

    return JsonResponse({'error': 'Invalid request data'}, status=400)