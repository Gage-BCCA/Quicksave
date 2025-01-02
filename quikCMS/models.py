from django.db import models

from feed.models import Game

# Create your models here.
class DevBlog(models.Model):
    title = models.CharField(max_length=255)
    related_game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    blurb = models.TextField(null=True)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title