from django.db import models

class WatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length = 100)
    rating = models.FloatField()
    release_date = models.CharField(max_length = 20)
    review = models.TextField()