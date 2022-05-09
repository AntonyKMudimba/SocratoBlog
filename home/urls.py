from django.urls import path

from home import views

urlpatterns = [
    path("home/", views.AuthorHome.as_view(), name="author_home"),
    path("profile/", views.Profile.as_view(), name="author_profile"),
    path("articles/", views.Articles.as_view(), name="author_articles"),
    path("create/", views.CreateArticle.as_view(), name="author_create"),

]
