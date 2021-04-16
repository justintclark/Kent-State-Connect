from django.forms import TextInput, Textarea
from django.db import models 
from embed_video.fields import EmbedVideoField

#user
class user(models.Model):
    username = models.CharField(max_length=191)

    def __str__(self):
        return self.username

#categories
class Category(models.Model):
    Cat_name=models.CharField(max_length=200)
    def __str__(self):
        return self.Cat_name

#parent model
class forum(models.Model):
    category = models.ForeignKey(Category,blank=False,on_delete=models.CASCADE)
    title= models.CharField(max_length=300)
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=10000,blank=False)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    upload=models.ImageField(null=True, blank=True, upload_to='images/')
    video=EmbedVideoField(blank=True)
    
    def __str__(self):
        return str(self.title)

#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    discuss = models.CharField(max_length=10000)
    upload=models.ImageField(null=True, blank=True, upload_to='images/')
    video=EmbedVideoField(blank=True)

    def __str__(self):
        return str(self.forum)