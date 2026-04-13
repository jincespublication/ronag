from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.conf import settings
import urllib.request
import json


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
    context = {"images":list(reversed(image)), "image_groups":image_group}
    return render(request, "gallery.html", context)

def membership(request):
    return render(request, 'membership.html')

def cce(request):

    return render(request, 'cce.html')

def ron(request):

    return render(request, 'ron.html')

def water_analysis(request):

    return render(request, 'water_analysis.html')

def donate(request):
    if request.method == "POST":
        email = request.POST.get("email")
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        custom_amount = request.POST.get("custom_amount")
        
        try:
            if custom_amount and float(custom_amount) > 0:
                final_amount = float(custom_amount)
            elif amount:
                final_amount = float(amount)
            else:
                final_amount = 10.0
        except (TypeError, ValueError):
            final_amount = 10.0
            
        amount_in_cents = int(final_amount * 100)
        
        url = "https://api.paystack.co/transaction/initialize"
        data = {
            "email": email,
            "amount": amount_in_cents,
            "callback_url": request.build_absolute_uri(reverse('success'))
        }
        data_json = json.dumps(data).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
        
        req = urllib.request.Request(url, data=data_json, headers=headers)
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                if result.get("status"):
                    auth_url = result["data"]["authorization_url"]
                    return redirect(auth_url)
        except urllib.error.URLError as e:
            error_msg = f"Payment initialization failed: {e.reason}"
            return render(request, "donate.html", {"error": error_msg})

    return render(request, 'donate.html')

def press_release(request):

    return render(request, 'press-release.html')

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

def success(request):
    return render(request, 'success.html')

def singleNews(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    context = {"post": post, "posts": list(reversed(posts))}
    return render(request, 'singleNews.html', context)

def singleProduct(request):
    return render(request, 'singleProduct.html')

