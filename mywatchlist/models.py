from django.db import models

# Create your models here.
class WatchlistItem(models.Model):
    watch_status = models.CharField(max_length=7)
    film_title = models.CharField(max_length=255)
    film_rating = models.IntegerField()
    film_release = models.CharField(max_length=17)
    film_review = models.CharField(max_length=280)
