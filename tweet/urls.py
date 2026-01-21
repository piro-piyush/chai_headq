from django.urls import path
from . import views

app_name = "tweet"

urlpatterns = [
    path("", views.feed, name="feed"),
    path("create/", views.create_tweet, name="create"),
    path("<int:tweet_id>/", views.view_tweet, name="view"),
    path("<int:tweet_id>/edit/", views.edit_tweet, name="edit"),
    path("<int:tweet_id>/delete/", views.delete_tweet, name="delete"),  # Delete a tweet
]
