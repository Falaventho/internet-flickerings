from django.db import models
from django.contrib.auth.models import AbstractUser


class FlickerUser(AbstractUser):
    pass

    def __str__(self):
        return self.username


class MediaRating(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Show(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    parent_show = models.ForeignKey(Show, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class MediaObject(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail_url = models.URLField()
    content_url = models.URLField()
    release_year = models.IntegerField()
    runtime = models.IntegerField()
    rating = models.ForeignKey(MediaRating, on_delete=models.PROTECT)
    season = models.ForeignKey(Season, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class GenreMediaLink(models.Model):
    media = models.ForeignKey(MediaObject, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class CastCrewMember(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Credited(models.Model):
    media = models.ForeignKey(MediaObject, on_delete=CASCADE)
    credited_member = models.ForeignKey(CastCrewMember, on_delete=CASCADE)
