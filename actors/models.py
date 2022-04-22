from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="actor_image", default="")
    date_of_birth = models.DateField()
    debut = models.DateField(null=True, blank=True)
    debut_movie = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
