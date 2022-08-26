# Create your views here.

from pytube import YouTube
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def download_yt_url(request):
    url = request.data['url']

    # https://youtube.com/watch?v=2lAe1cqCOXo
    yt = YouTube(url)

    list_fo_options = []

    for i in yt.streams:
        print(i.__dict__)
        item = i.__dict__
        slected_item = {
            'url': item['url'],
            'itag': item['itag'],
            'mime_type': item['mime_type'],
            # 'fps': item['fps'],
            'resolution': item['resolution'],
        }

        list_fo_options.append(slected_item)

    return Response(list_fo_options)
