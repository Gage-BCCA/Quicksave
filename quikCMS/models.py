from django.db import models

from feed.models import Game

# Create your models here.
class DevBlog(models.Model):
    title = models.CharField(max_length=255)
    related_game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    blurb = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title