from django.urls import path

from . import views


urlpatterns = [
    path("index.html", views.index, name="index"),
    path("", views.index, name="index"),
    path("about.html", views.about, name="about"),
    path("contact.html", views.contact, name="contact"),
    path("news.html", views.news, name="news"),
    path("singleNews.html/<int:post_id>", views.singleNews, name="singleNews")
]
