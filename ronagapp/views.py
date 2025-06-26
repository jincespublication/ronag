from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.
posts = Post.objects.all()
online_posts = OnlinePost.objects.all()
post = {"posts": list(reversed(posts)), "onlinePosts": list(reversed(online_posts))}



def index(request):

    return render(request, 'index.html', post)

def about(request):
    team = Team.objects.all()
    context = {'teams': team}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')


def gallery(request):
    image = Gallery.objects.all()
    image_group = ImageGroup.objects.all()
    context = {"images":image, "image_groups":image_group}
    return render(request, "gallery.html", context)

def membership(request):
    return render(request, 'membership.html')



def article(request):
    context = {"posts": posts}
    return render(request, 'article.html', context)

def article2(request):
    context = {"posts": posts}
    return render(request, 'article2.html', context)


def news(request):
    return render(request, 'news.html', post)

def online(request):
    
    return render(request, 'online.html', post)

def singleNews(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post, "posts": posts}
    return render(request, 'singleNews.html', context)

def singleProduct(request):
    return render(request, 'singleProduct.html')

