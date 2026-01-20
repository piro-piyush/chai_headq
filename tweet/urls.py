
from django.urls import path
from . import views


# Url : localhost:8080/tweet/
urlpatterns = [
    path('',views.tweet,name='tweet'),
    path('create-tweet/',views.create_tweet,name='create-tweet'),
    path('edit-tweet/',views.edit_tweet,name='edit-tweet'),
    path('<int:tweet_id>/',views.edit_tweet,name='view-tweet'),
]
