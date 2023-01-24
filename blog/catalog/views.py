from django.shortcuts import render
from .models import Blogger, Post, Comment

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_bloggers = Blogger.objects.all().count()
    num_posts = Post.objects.all().count()
    num_comments = Comment.objects.all().count()

    context = {
        'num_bloggers': num_bloggers,
        'num_posts': num_posts,
        'num_comments': num_comments,
    }

    # Render the HTML template index.html with the data in the contex variable
    return render(request, 'index.html', context=context)
