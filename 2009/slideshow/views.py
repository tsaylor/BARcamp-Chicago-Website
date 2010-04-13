from django.shortcuts import render_to_response
from slideshow.models import room, message, talk
import datetime, urllib, random
from django.utils.simplejson.decoder import JSONDecoder


def viewSlide(request, rid, sid):
    if sid == '1': # welcome slide
        return render_to_response('slideshow/welcome.html', {'sid':2, 'rid':rid})
    elif sid == '2': # current slide
        r = room.objects.get(pk=rid)
        t = talk.objects.filter(day__exact=datetime.date.today()
                        ).filter(time__in=(datetime.datetime.today().hour, datetime.datetime.today().hour+1)
                        ).filter(room__exact=r)
        return render_to_response('slideshow/current.html', {'room':r, 'sid':3, 'talk':t, 'rid':rid})
    elif sid == '3': # other rooms slide
        r = room.objects.get(pk=rid)
        t = talk.objects.filter(day__exact=datetime.date.today()
                        ).filter(time__exact=datetime.datetime.today().hour
                        ).exclude(room__exact=r)
        if message.objects.filter(msg_type__exact='ann').count() > 0:
            next_sid = 4
        elif message.objects.filter(msg_type__exact='spr').count() > 0:
            next_sid = 5
        else:
            next_sid = 6
        return render_to_response('slideshow/other_rooms.html', {'talk':t, 'sid':next_sid, 'rid':rid})
    elif sid == '4': # announcements
        a = message.objects.filter(msg_type__exact='ann')
        if message.objects.filter(msg_type__exact='spr').count() > 0:
            next_sid = 5
        else:
            next_sid = 6
        return render_to_response('slideshow/announce.html', {'msg':a[0], 'sid':next_sid, 'rid':rid})
    elif sid == '5': # sprints
        a = message.objects.filter(msg_type__exact='spr')
        return render_to_response('slideshow/sprints.html', {'msg':a[0], 'sid':6, 'rid':rid})
    elif sid == '6': # sponsor
        # get a random page 1-641 size 1 and extract the photo id
        j = urllib.urlopen('''http://www.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&format=json&api_key=d82fbb3d032a627fe25fe4c5f1080b68&nojsoncallback=1&group_id=1023481@N23&per_page=1&page=%d''' % (random.randint(1,641)))
        json = JSONDecoder().decode(j.read())
        photo_id = json['photos']['photo'][0]['id']
        # get the photo and extract the image url
        j = urllib.urlopen('''http://www.flickr.com/services/rest/?method=flickr.photos.getSizes&format=json&api_key=d82fbb3d032a627fe25fe4c5f1080b68&nojsoncallback=1&photo_id=%s''' % (photo_id))
        json = JSONDecoder().decode(j.read())
        pic_url = json['sizes']['size'][3]['source']
        return render_to_response('slideshow/sponsor.html', {'pic':pic_url, 'sid':1, 'rid':rid})
    else:
        return render_to_response('slideshow/announce.html', {'msg':'rid=%s,sid=%s'%(rid,sid), 'rid':rid})