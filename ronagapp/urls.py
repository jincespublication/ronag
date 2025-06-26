from django.urls import path

from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("article", views.article, name="article"),
    path("article2", views.article2, name="article2"),
    path("news", views.news, name="news"),
    path("online", views.online, name="online"),
    path("gallery", views.gallery, name="gallery"),
    path("membership", views.membership, name="membership"),
    path("singleNews/<int:post_id>", views.singleNews, name="singleNews")
]
