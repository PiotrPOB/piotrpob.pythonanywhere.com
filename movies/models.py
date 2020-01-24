from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    year = models.IntegerField(default=1900)
    poster = models.ImageField(upload_to='poster', default=None)

    def __str__(self):
        return self.title

