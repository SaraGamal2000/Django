from django.db import models
from track.models import *
# Create your models here.
class Trainee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200,null=False)
    id_track=models.ForeignKey("track.Track", on_delete=models.CASCADE)
    image= models.ImageField(upload_to='media/',null=True)
    
    
    @classmethod
    def create_trainee(cls,id,name,id_track,image):
        trainee_obj = Trainee(
            id=id,
            name=name,
            id_track=id_track,
            image=image
        )
        trainee_obj.save()
        
        
    @classmethod
    def delete_trainee(cls,id):
        cls.objects.filter(pk=id).delete()
        
        
    def update_trainee(self,id,name,id_track,image):
        self.id=id,
        self.name=name,
        self.id_track=id_track
        self.image=image
        self.save()
       
