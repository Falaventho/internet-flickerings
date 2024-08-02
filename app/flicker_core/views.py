from django.shortcuts import render, redirect
from flicker_core.models import MediaObject


# Create your views here.
def home(request):
    return redirect('/browse/')


def browse(request):
    return render(request, 'flicker_core/browse.html')


def watch(request, media_id):
    media_object = MediaObject.objects.get(id=media_id)
    return render(request, 'flicker_core/watch.html', {
        'title': media_object.title,
        'content_url': media_object.content_url,
    })


def devwatch(request):
    return render(request, 'flicker_core/devwatch.html')
