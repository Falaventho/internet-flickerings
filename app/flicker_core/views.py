from django.shortcuts import render, redirect
from flicker_core.models import MediaObject


# Create your views here.
def home(request):
    return redirect('browse')


def browse(request):
    cards = MediaObject.objects.all()
    sections = [
        {
            "title": "Example Section",
            "cards": cards
        }
    ]
    return render(request, 'flicker_core/browse.html', {'sections': sections})


def watch(request, media_id):
    media_object = MediaObject.objects.get(id=media_id)
    return render(request, 'flicker_core/watch.html', {
        'title': media_object.title,
        'content_uri': media_object.content_uri,
    })
