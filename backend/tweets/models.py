from django.db import models


class Tweet(models.Model):
    text        = models.CharField(max_length=50)
    name        = models.CharField(max_length=20)
    datetime    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        tweet_repr = self.text if len(self.text) < 20 else self.text[:20]+'...'
        return "%s (%s)" %(tweet_repr, self.name)

