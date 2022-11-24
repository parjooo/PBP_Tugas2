from django.db import models

class WatchList(models.Model):
    watched = models.CharField(max_length=3)
    title = models.TextField()
    rating = models.IntegerField()
    release_date = models.TextField()
    review = models.TextField()
