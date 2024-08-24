from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=200,null=False)
    lname = models.CharField(max_length=200,null=False)
    email = models.EmailField(max_length=254, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    image= models.ImageField(upload_to='media/',null=True)
    # ,Blank=True
    
    @classmethod
    def create_acc(cls,id,fname,lname,email,password,image):
        acc_obj = Account(
            id=id,
            fname=fname,
            lname=lname,
            email=email,
            password=password,
            image=image
        )
        acc_obj.save()
        
        
    @classmethod
    def delete_acc(cls,id):
        cls.objects.filter(pk=id).delete()
        
        
    def update_acc(self,id,fname,lname,email, password,image):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.email=email
        self.password=password
        self.image=image
        self.save()
       
    # def getimage(self):
    #     return f'/media/{self.image}'

        