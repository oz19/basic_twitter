from rest_framework.generics import ListCreateAPIView

from tweets.models import Tweet
from .serializers import TweetSerializer


class ListCreateTweet(ListCreateAPIView):
    queryset            = Tweet.objects.all()
    serializer_class    = TweetSerializer

