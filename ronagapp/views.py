from django.shortcuts import get_object_or_404, render

from .models import *

# Create your views here.
posts = Post.objects.all()
post = {"posts": posts}
def index(request):
    return render(request, 'index.html', post)

def about(request):
    team = Team.objects.all()
    context = {'teams': team}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def article(request):
    return render(request, 'article.html')


def news(request):
    return render(request, 'news.html', post)

def singleNews(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post, "posts": posts}
    return render(request, 'singleNews.html', context)

def singleProduct(request):
    return render(request, 'singleProduct.html')

