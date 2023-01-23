import datetime

from django.db import models
from django.urls import reverse

class Blogger(models.Model):
    """Model representing a author of posts."""

    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=1000, help_text='Enter a brief bio of the author.')

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this author."""

        return reverse('blogger-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""

        return self.title

class Post(models.Model):
    """Model representing a blog of post."""

    title = models.CharField(max_length=100)
    post_date = datetime.date
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000, help_text='Enter a text of your post.')

    def __str__(self):

        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this post."""

        return reverse('post-detail', args=[str(self.id)])

class Comment(models.Model):
    """Model representing a comment."""

    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null=True)
    comment_date = datetime.datetime
    description = models.TextField(max_length=1000, help_text='Enter a description of your comment.')

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this comment."""

        return reverse('post-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""

        return self.title
