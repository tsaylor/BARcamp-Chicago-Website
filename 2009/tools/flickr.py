from django.utils.simplejson.decoder import JSONDecoder
#http://www.flickr.com/services/rest/?method=flickr.groups.pools.getPhotos&format=json&api_key=d2cdec3fd31212ca7ef385287f050748&nojsoncallback=1&group_id=1023481@N23&per_page=10
JSONDecoder().decode(json_string)