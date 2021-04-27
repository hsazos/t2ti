from django.urls import path
from .views import Artist_list, specific_artist, artist_albums, artist_tracks_GET, \
    get_all_albums, album_by_id, tracks_by_album, all_tracks, track_by_id, \
        play_all_album_tracks, play_all_artist_tracks, play_track

urlpatterns = [
    path('artists/', Artist_list),
    path('artists/<artist_id>', specific_artist),
    path('artists/<artist_id>/albums', artist_albums),
    path('artists/<artist_id>/tracks', artist_tracks_GET),
    path('albums', get_all_albums),
    path('albums/<album_id>', album_by_id),
    path('albums/<album_id>/tracks', tracks_by_album),
    path('tracks', all_tracks),
    path('tracks/<track_id>', track_by_id),
    path("artists/<artist_id>/albums/play", play_all_artist_tracks),
    path('albums/<album_id>/tracks/play', play_all_album_tracks),
    path('tracks/<track_id>/play', play_track)
]
