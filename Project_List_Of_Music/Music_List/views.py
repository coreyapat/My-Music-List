from django.shortcuts import render
from .models import Song
from .serializers import SongSerializer
from rest_framework.views import APIView
from rest_framework.reponse import Response
from rest_framework import status

# Create your views here.
class SongList(APIView):

    def get(self, request):
        song = Song.objects.aall()
        serializer = SongSerializer(song, many=True)
        return Response(serializer.data)