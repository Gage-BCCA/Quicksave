from django.db import models
from django.contrib.auth.models import User

from feed.models import Game, GenericPost

# Create your models here.
class ExtendedUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True)
    headliner = models.CharField(max_length=255, null=True)
    bio = models.TextField(null=True)
    location = models.CharField(max_length=50, null=True)
    followed_users = models.ManyToManyField(User, related_name="followed_users")
    followed_games = models.ManyToManyField(Game, related_name="followed_games")
    bookmarked_posts = models.ManyToManyField(GenericPost, related_name="bookmarked_posts")


