from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from base64 import b64encode


#Chequea todos los errores que puede tener artista en el POST.
def error_checker_artista(artista):
  #Reviso si es Bad Request
  llaves = artista.keys()
  if "name" not in llaves or "age" not in llaves:
    return ({"error": 400})
  if type(artista["name"]) != str or type(artista["age"]) != int:
    return ({"error": 400})
  #Luego reviso si el artista ya existe
  artistas = Artist.objects.filter(name=artista["name"])
  if len(artistas) > 0:
    return ({"error": 409})
  #Pasó todas las pruebas asique se va.
  else:
    return ({"error": 0})

def error_checker_album(artist_id ,album):
  llaves = album.keys()
  if "name" not in llaves or "genre" not in llaves:
    return ({"error": 400})
  if type(album["name"]) != str or type(album["genre"]) != str:
    return ({"error": 400})
  album = Album.objects.filter(name=album["name"])
  print("LO PRINTIE")
  print(album)
  if len(album) > 0:
    return({"error": 409})
  artista = Artist.objects.filter(id=artist_id)
  if len(artista) == 0:
    return ({"error": 422})
  else:
    return({"error": 0})

def error_checker_track(album_id, track):
  llaves = track.keys()
  if "name" not in llaves or "duration" not in llaves:
    return ({"error": 400})
  if type(track["name"]) !=str :
    return ({"error": 400})
  cancion = Track.objects.filter(name=track["name"])
  if len(cancion) > 0:
    return ({"error": 409})
  album = Album.objects.filter(id=album_id)
  if len(album) == 0:
    return ({"error":422})
  else:
    return ({"error": 0})