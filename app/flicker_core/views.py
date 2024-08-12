from django.shortcuts import render, redirect
from flicker_core.models import MediaObject


# Create your views here.
def home(request):
    return redirect('browse')


def browse(request):
    example_cards = MediaObject.objects.all()
    recent_ids = request.session.get('recents', [])
    recent_cards = MediaObject.objects.filter(id__in=recent_ids)
    sections = [
        {
            "title": "Example Section",
            "cards": example_cards,
        },
        {
            "title": "Recently Viewed",
            "cards": recent_cards
        }
    ]
    return render(request, 'flicker_core/browse.html', {'sections': sections})


def watch(request, media_id):
    media_object = MediaObject.objects.get(id=media_id)

    recently_viewed = request.session.get('recents', [])

    if media_id not in recently_viewed:
        recently_viewed.append(media_id)
        request.session['recents'] = recently_viewed

    return render(request, 'flicker_core/watch.html', {
        'title': media_object.title,
        'content_uri': media_object.content_uri,
    })
