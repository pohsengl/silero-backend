from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tts.corefunc import generate_tts

# Create your views here.
@api_view(['POST'])
def tts(request):
    print(request.data)
    print(request.get_host())
    audioPath=generate_tts(request.data["text"])
    audioURL=f'http://{request.get_host()}/{audioPath}'
    data={
        "text": request.data["text"],
        "audioURL": audioURL
    }
    return Response(data)