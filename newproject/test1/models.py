from  django.contrib.auth.models import User
from django.db import models
from  django.db import  migrations

# Create your models here.
class  Service(models.Model):
    #idservice = models.BigIntegerField(max_length=100,unique='true')
    nameservice= models.CharField(max_length=50)
    def __str__(self):
        return  self.nameservice



c