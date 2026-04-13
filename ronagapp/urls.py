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
    path("cce", views.cce, name="cce"),
    path("ron", views.ron, name="ron"),
    path("water_analysis", views.water_analysis, name="water_analysis"),
    path("donate", views.donate, name="donate"),
    path("success", views.success, name="success"),
    path("sucess", views.success, name="sucess"),   # Added to catch the previous typo
    path("press-release", views.press_release, name="press-release"),
    path("singleNews/<int:post_id>", views.singleNews, name="singleNews")
]
