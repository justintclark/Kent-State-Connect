from django.forms import TextInput, Textarea
from django.db import models 
    
#parent model
class forum(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200,null=False)
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=10000,blank=False)
    #link = models.CharField(max_length=100 ,null =True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)

#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    discuss = models.CharField(max_length=10000)

    def __str__(self):
        return str(self.forum)