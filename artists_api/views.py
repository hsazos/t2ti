from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .models import Artist, Album, Track
from .serializers import ArtistSerializer, AlbumSerializer, TrackSerializer
from base64 import b64encode
from .error_checker import error_checker_album, error_checker_artista, error_checker_track
from django.shortcuts import get_object_or_404, get_list_or_404
# Create your views here.

def funcionilla(serializerd):
  for artista in serializerd.data:
    aux =  artista["self_url"]
    del artista["self_url"]
    artista["self"] = aux
  return serializerd


@csrf_exempt
def Artist_list(request):

  if request.method =='GET':
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists, many=True)
    serializer = funcionilla(serializer)
    return JsonResponse(serializer.data, safe=False, status=200)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    error = error_checker_artista(data)
    if error["error"] != 0 and error["error"] != 409:
      return JsonResponse({"error": "error"}, status=error["error"])
    if error["error"] == 409:
      buscado = Artist.objects.filter(name=data["name"])
      serializer = ArtistSerializer(buscado[0])
      serializer_data = serializer.data
      serializer_data["self"] = serializer_data["self_url"]
      serializer_data.pop("self_url")

      return JsonResponse(serializer_data, safe=False, status=409)
    data["id"] = (b64encode(data['name'].encode()).decode('utf-8'))[0:22]
    serializer = ArtistSerializer(data=data)
    if serializer.is_valid( ):
      
      serializer.validated_data["albums"] = "https://t2ti.herokuapp.com/artists/" + serializer.validated_data["id"] +"/albums"
      serializer.validated_data["tracks"] = "https://t2ti.herokuapp.com/artists/" + serializer.validated_data["id"] +"/tracks"
      serializer.validated_data["self_url"] = "https://t2ti.herokuapp.com/artists/" + serializer.validated_data["id"]
      serializer.save()
      serializer.validated_data["self"] = serializer.validated_data["self_url"]
      del serializer.validated_data["self_url"]
      return JsonResponse(serializer.validated_data, status=201)


@csrf_exempt
def specific_artist(request, artist_id):
  
  if request.method == 'GET':
    artista = get_object_or_404(Artist,id = artist_id)
    if not artista:
      return JsonResponse({"Artist does not exist": "Artista no existe"}, status=404)
    else:
      serializer = ArtistSerializer(artista[0])
      serializer_data = serializer.data
      serializer_data["self"] = serializer_data["self_url"]
      del serializer_data["self_url"]
      return JsonResponse(serializer_data, status=200)
  elif request.method == 'DELETE':
    artista = Artist.objects.filter(id = artist_id)
    if len(artista) == 0:
      return JsonResponse({}, status=404)
    else:
      artista.delete()
      return JsonResponse({}, status=204)
  

@csrf_exempt
def artist_albums(request, artist_id):
  if request.method == 'GET':
    artista = get_object_or_404(Artist, id=artist_id)
    albumes = Album.objects.filter(artist_id=artist_id)
    if not artista:
      return JsonResponse({"Artist does not exist": "Artista no existe"}, status=404)
    else:
      serializer = AlbumSerializer(albumes, many=True)
      serializer = funcionilla(serializer)
      return JsonResponse(serializer.data,  status=200, safe=False)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    error = error_checker_album(artist_id ,data)
    if error["error"] != 0 and error["error"] !=409:
      return JsonResponse({"error": "error"}, status=error["error"])
    if error["error"] == 409:
      buscado = Album.objects.filter(name=data["name"])
      serializer = AlbumSerializer(buscado[0])
      serializer_data = serializer.data
      serializer_data["self"] = serializer_data["self_url"]
      serializer_data.pop("self_url")

      del serializer.data["self_url"]
      return JsonResponse(serializer_data, safe=False, status=409)
    string = data["name"] + ":" + str(artist_id)
    resultado = (b64encode(string.encode()).decode('utf-8'))
    resultado = resultado[0:22]
    data["id"] = resultado
    data["artist_id"] = artist_id
    serializer = AlbumSerializer(data=data)
    if serializer.is_valid():
      serializer.validated_data["artist"] = "https://t2ti.herokuapp.com/artist/" + str(artist_id)
      serializer.validated_data["tracks"] = "https://t2ti.herokuapp.com/albums/" + serializer.validated_data["id"] + "/tracks"
      serializer.validated_data["self_url"] = "https://t2ti.herokuapp.com/albums/" + serializer.validated_data["id"]
      serializer.save()
      serializer.validated_data["self"] = serializer.validated_data["self_url"]
      del serializer.validated_data["self_url"]
      serializer.validated_data["artist_id"] = serializer.validated_data["artist_id"].id
      return JsonResponse(serializer.validated_data, status=201, safe=False)


@csrf_exempt
def artist_tracks_GET(request, artist_id):
  if request.method ==["GET"]:
    artista = Artist.objects.filter(id = artist_id)
    tracks = Track.objects.filter(artist="/artists/" + artist_id)
    if len(artista) == 0:
      return JsonResponse({"error": "error"}, status = 422)
    serializer = TrackSerializer(tracks, many=True)
    serializer = funcionilla(serializer)
    return JsonResponse(serializer.data, status =200, safe=False)
    
@csrf_exempt
def get_all_albums(request):
  if request.method == "GET":
    albums = Album.objects.all()
    if len(albums) == 0:
      return JsonResponse({}, status=200)
    serializer = AlbumSerializer(albums, many=True)
    serializer = funcionilla(serializer)
    return JsonResponse(serializer.data, status=200, safe=False)
@csrf_exempt
def album_by_id(request, album_id):
  album = get_object_or_404(Albums, id=album_id)
  if request.method == "GET": 
    if len(album) == 0:
      return JsonResponse({}, status=404)
    serializer = AlbumSerializer(album[0])
    serializer_data = serializer.data
    serializer_data["self"] = serializer_data["self_url"]
    del serializer_data["self_url"]
    return JsonResponse(serializer_data, status=200)

  elif request.method == "DELETE":
    if len(album) == 0:
      return JsonResponse({}, status=404)
    else:
      album.delete()
      return JsonResponse({}, status=204)

@csrf_exempt
def tracks_by_album(request, album_id):
  album = Album.objects.filter(id=album_id)
  if request.method == "GET":
    tracks = Track.objects.filter(album_id=album_id)
    if len(tracks) == 0:
      return JsonResponse({}, status=404)
    serializer = TrackSerializer(tracks, many=True)
    serializer = funcionilla(serializer)
    return JsonResponse(serializer.data, status=200, safe=False)

  if request.method == "POST":
    data = JSONParser().parse(request)
    error = error_checker_track(album_id, data)
    if error["error"] != 0 and error["error"] !=409:
      return JsonResponse({"error": "error"}, status=error["error"])
    if error["error"] == 409:
      buscado = Track.objects.filter(name=data["name"])
      serializer = TrackSerializer(buscado[0])
      serializer_data = serializer.data
      serializer_data["self"] = serializer_data["self_url"]
      serializer_data.pop("self_url")

      return JsonResponse(serializer_data, safe=False, status=409)
    string = (data["name"] + ":" + str(album_id))
    resultado = (b64encode(string.encode()).decode('utf-8'))
    resultado = resultado[0:22]
    data["id"] = resultado
    data["album_id"] = album_id
    serializer = TrackSerializer(data=data)
    if serializer.is_valid():
      serializer.validated_data["times_played"] = 0
      serializer.validated_data["album"] = "https://t2ti.herokuapp.com/albums/" + str(album_id)
      serializer.validated_data["self_url"] = "https://t2ti.herokuapp.com/tracks/" +str(serializer.validated_data["id"])
      serializer.validated_data["artist"] = "https://t2ti.herokuapp.com/artists/" + str(album_id)
      serializer.save()
      serializer.validated_data["self"] = serializer.validated_data["self_url"]
      del serializer.validated_data["self_url"]
      serializer.validated_data["album_id"] = serializer.validated_data["album_id"].id
      return JsonResponse(serializer.validated_data, status=201)
    else:
      return JsonResponse({}, status=400)

@csrf_exempt
def all_tracks(request):
  tracks = Track.objects.all()
  if len(tracks) == 0:
    return JsonResponse({}, status=200)
  serializer = TrackSerializer(tracks, many=True)
  serializer = funcionilla(serializer)
  return JsonResponse(serializer.data, status=200, safe=False)
  
@csrf_exempt
def track_by_id(request, track_id):
  tracks = get_object_or_404(Track, id=track_id)

  if request.method == "GET":
    if len(tracks) == 0:
      return JsonResponse({}, status=404)
    serializer = TrackSerializer(tracks[0])
    serializer_data = serializer.data
    serializer_data["self"] = serializer_data["self_url"]
    del serializer_data["self_url"]
    return JsonResponse(serializer_data, status=200, safe=False)

  elif request.method == "DELETE":
    if len(tracks) == 0:
      return JsonResponse({}, status=404)
    else:
      tracks.delete()
      return JsonResponse({}, status=204)

@csrf_exempt
def play_all_artist_tracks(request, artist_id):
  artist = Artist.objects.filter(id=artist_id)
  if len(artist) == 0:
    return JsonResponse({}, status=404)
  albums = Album.objects.filter(artist_id=artist_id)
  for album in albums:
    tracks = Track.objects.filter(album_id=album.id)
    for track in tracks:
      track.times_played +=1
      track.save()
  return JsonResponse({}, status=200)
@csrf_exempt
def play_all_album_tracks(request, album_id):
  album = Album.objects.filter(id=album_id)
  if len(album) == 0:
    return JsonResponse({}, status=404)

  tracks = Track.objects.filter(album_id=album_id)
  for cancion in tracks:
    cancion.times_played +=1
    cancion.save()
  return JsonResponse({}, status=200)
@csrf_exempt
def play_track(request, track_id):
  track = Track.objects.filter(id=track_id)
  if len(track) == 0:
    return JsonResponse({}, status=404)
  track = track[0]
  track.times_played +=1
  track.save()
  return JsonResponse({}, status=200)