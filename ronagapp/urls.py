from django.urls import path

from . import views


urlpatterns = [
    path("index.html", views.index, name="index.html"),
    path("", views.index, name="index.html"),
    path("about.html", views.about, name="about.html"),
    path("contact.html", views.contact, name="contact.html"),
    path("news.html", views.news, name="news.html"),
    path("singleNews.html", views.singleNews, name="singleNews.html"),
    path("singleProduct.html", views.singleProduct, name="singleProduct.html"),
    path("singleNews.html/<int:post_id>", views.singleNews, name="singleNews")
]
