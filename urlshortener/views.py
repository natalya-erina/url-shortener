import string
import time

from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.template import loader
from django.template.context_processors import csrf
from django.views import generic
from django.utils.timezone import localtime, now
from django.views.decorators.csrf import csrf_exempt
import random

from urlshortener.models import URL, Image

def generate_short_url(request):
    short_url = request.META['HTTP_HOST'] + '/short_url/'
    for _ in range(0, 6):
        ch = random.choice(string.ascii_letters + string.digits)
        short_url += str(ch)
    return short_url


def contains(short_url):
    return URL.objects.all().filter(short_url=short_url).exists()


@csrf_exempt
def index(request):
    if request.method == 'POST':
        short_url = generate_short_url(request)
        while contains(short_url):
            short_url = generate_short_url(request)
        URL.objects.create(source_url=request.POST.get("long_url"), created_at=now(), short_url=short_url)
        return render_to_response('urlshortener/url.html', {'short_url':short_url})
    else:
        latest_urls_list = URL.objects.all().order_by('-created_at')
        return render_to_response('urlshortener/index.html', {'latest_urls_list':latest_urls_list})


@csrf_exempt
def redirect_and_show_ad(request):
    images = []
    for i in range(1,5):
        img = Image.objects.create(image_url='/static/'+ str(i) + '.jpg')
        images.append(img.image_url)
    path = request.META['HTTP_HOST'] + request.get_full_path()
    original_url = ''
    for u in URL.objects.all():
        if u.short_url.__eq__(path):
            original_url = u.source_url
            break
    response = render_to_response('urlshortener/show_ad.html', {'images': images})
    response.set_cookie('orig_url', original_url)
    response.set_cookie('time', 15)
    return response