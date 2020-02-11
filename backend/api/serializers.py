from rest_framework import serializers

from tweets.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Tweet
        fields  = ('name', 'text', 'datetime')
