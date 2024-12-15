from django.db import models
from django.contrib.auth.models import User

class Keyword(models.Model):
    keyword = models.CharField(max_length=50)


class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    blurb = models.TextField()
    description = models.TextField()
    developers = models.ManyToManyField(User)
    price = models.CharField(max_length=25, null=True)
    release_date = models.DateField(null=True)
    title_img = models.ImageField(upload_to='games/title-img/', null=True)

    def __str__(self):
        return self.title
    

class DevBlog(models.Model):
    title = models.CharField(max_length=255)
    related_game = models.ForeignKey(Game, null=False, on_delete=models.CASCADE)
    blurb = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.title

class GenericPost(models.Model):
    """
    Generic Model for posts and replies for comments.

    Has a self-referential Immediate parent field that allows for 
    an arbitrary amount of replies on posts or other replies. 
    
    When navigating to a post,
    a lookup can be done of the top level parent to grab all
    related comments, and then the immediate parent field can
    be used to organize those comments properly.
    """
    
    date_posted = models.DateTimeField(auto_now=True)
    post_content = models.TextField()
    keywords = models.ManyToManyField(Keyword, default=None)
    related_game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
    top_level_parent = models.ForeignKey('GenericPost', on_delete=models.CASCADE, null=True)
    immediate_parent = models.ForeignKey('GenericPost', on_delete=models.CASCADE, null=True, related_name="child_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, default=None, related_name="likes")
    dislikes = models.ManyToManyField(User, default=None, related_name="dislikes")

    def __str__(self):
        return self.post_content

    @property
    def num_comments(self):
        """Returns the total number of comments for a post"""
        return GenericPost.objects.filter(top_level_parent = self.id).count()
    
    @property
    def num_likes(self):
        """Returns the total number of likes for a post"""
        return self.likes.all().count()
    
    @property
    def num_dislikes(self):
        """Returns the total number of dislikes for a post"""
        return self.dislikes.all().count()
    
    @property
    def all_comments(self):
        return GenericPost.objects.filter(immediate_parent=self.id)