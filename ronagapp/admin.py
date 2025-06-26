from django.contrib import admin
# from .models import Team, Post, OnlinePost
from .models import *

# Register your models here.
admin.site.register(Team)
admin.site.register(Post)
admin.site.register(OnlinePost)
admin.site.register(Gallery)
admin.site.register(ImageGroup)