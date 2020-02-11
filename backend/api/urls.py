from django.urls import path

from api.views import ListCreateTweet


urlpatterns = [
    path('tweets/', ListCreateTweet.as_view(), name='tweet-list-create'),
]
