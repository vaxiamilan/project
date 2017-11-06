from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_album=Album.objects.all()
    #html=''
    #for album in all_album:
    #   url='/music/' + str(album.id) + '/'
    #    html+='<a href="'+ url +'">' + album.album_title + '</a><br>'
    #return HttpResponse(html)
    template = loader.get_template('music/index.html')
    context={
        'all_albums':all_album,
    }
    return HttpResponse(template.render(context,request))

    #return HttpResponse("<h1>this will be list of all Albums</h1>")
def detail(request, album_id):
    return HttpResponse("<h2> Details for Album id: " + str(album_id) + "</h2>")
