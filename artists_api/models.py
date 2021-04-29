from django.db import models

# Create your models here.
class Artist(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    albums = models.CharField(max_length=200, blank=True, null=True)
    tracks = models.CharField(max_length=200, blank=True, null=True)
    self_url = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
      return self.name


class Album(models.Model):
  id = models.CharField(primary_key=True, max_length=200)
  artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  genre = models.CharField(max_length=200)
  artist = models.CharField(max_length=200, blank=True, null=True)
  tracks = models.CharField(max_length=200, blank=True, null=True)
  self_url = models.CharField(max_length=200, blank=True, null=True)

  def __str__(self):
    return self.name

class Track(models.Model):
  id = models.CharField(primary_key=True,max_length=200)
  album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  duration = models.FloatField()
  times_played = models.IntegerField(blank=True, null=True)
  artist = models.CharField(max_length=200, blank=True, null=True)
  album = models.CharField(max_length=200, blank=True, null=True)
  self_url = models.CharField(max_length=200, blank=True, null=True)

def __str__(self):
  return self.name