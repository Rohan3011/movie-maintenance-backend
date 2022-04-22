from django.db import models

LANGUAGE_CHOICES = (
    ('EN', 'ENGLISH'),
    ('HI', 'HINDI'),
    ('TA', 'TAMIL'),
    ('TE', 'TELUGU')
)

GENRE_CHOICES = (
    ('AC', 'ACTION'),
    ('DR', 'DRAMA'),
    ('RO', 'ROMANCE'),
    ('CO', 'COMEDY'),
    ('TH', 'THRILLER')
)


class Genre(models.Model):
    name = models.CharField(choices=GENRE_CHOICES, max_length=2)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    image = models.ImageField(upload_to="movies_thumbnails")
    genre = models.ForeignKey(Genre, related_name="genre", null=True,
                              blank=True, on_delete=models.SET_NULL)
    date_of_release = models.DateField()

    def __str__(self) -> str:
        return self.title
