from django.db import models
from track.models import *
# Create your models here.
class Trainee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200,null=False)
    id_track=models.ForeignKey("track.Track", on_delete=models.CASCADE)
