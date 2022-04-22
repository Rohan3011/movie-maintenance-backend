from django.db import models

from movies.models import Movie
from actors.models import Actor


class Cast(models.Model):
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(
        Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=255, null=True, blank=True)
