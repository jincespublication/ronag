from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length = 40)
    profile = models.CharField(max_length = 200)
    description = models.CharField(max_length = 1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="team/")

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url
    

class Post(models.Model):
    title = models.CharField(max_length = 150)
    paragraph1 = models.TextField(null=True, blank=True)
    paragraph2 = models.TextField(max_length = 100000, null=True, blank=True)
    paragraph3 = models.TextField(max_length = 100000, null=True, blank=True)
    paragraph4 = models.TextField(max_length = 100000, null=True, blank=True)
    paragraph5 = models.TextField(max_length = 100000, null=True, blank=True)
    paragraph6 = models.TextField(max_length = 100000, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="posts/")
    image2 = models.ImageField(null=True, blank=True, upload_to="posts/")
    image3 = models.ImageField(null=True, blank=True, upload_to="posts/")
    date = models.DateTimeField(_("Date"), auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = " " 
        return url