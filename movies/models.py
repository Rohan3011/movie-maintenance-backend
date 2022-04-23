from django.db import models

LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('HI', 'HINDI'),
    ('TA', 'TAMIL'),
    ('TE', 'TELUGU')
)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    image = models.ImageField(upload_to="movies_thumbnails")
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return self.title
