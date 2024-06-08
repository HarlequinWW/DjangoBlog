from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.FileField(default='', blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
