from django.shortcuts import render, redirect
from flicker_core.models import MediaObject
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def home(request):
    return redirect('browse')


@login_required
def browse(request):
    example_cards = MediaObject.objects.all()

    # ? recents cleanup firing on browse seems more reasonable than on watch, review
    recent_ids = request.session.get('recents', [])
    recent_ids = recent_ids[:10]
    request.session['recents'] = recent_ids

    recent_cards = MediaObject.objects.filter(id__in=recent_ids)
    recent_cards = list(reversed(recent_cards))
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


@login_required
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
