from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserPostForm
from .models import GenericPost
from accounts.models import ExtendedUserData

# Game Imports
from .models import Game
from .forms import GameCreationForm


# Create your views here.
@login_required(login_url='login')
def homepage_view(request):
    """Returns the main feed page. Here is where the 'algorithm' is used to deliver front page material"""

    form = UserPostForm()
    all_posts = GenericPost.objects.all().filter(immediate_parent__isnull = True)
    context = {'form': form,
               'posts': all_posts}
    return render(request, 'index.html', context=context)

@login_required
def process_post(request):
    """Processes posts and saves them to the database"""

    # Redirect to homepage early if HTTP method is not POST
    if request.method != "POST":
        return redirect('homepage')
    
    form = UserPostForm(request.POST)
    if form.is_valid():
        user = request.user
        text_content = form.cleaned_data.get('post_content')

        new_post = GenericPost(author=user,
                               post_content=text_content,
                               top_level_parent=None,
                               immediate_parent=None,
                               )
        new_post.save()
        return redirect('homepage')

@login_required
def process_comment(request):
    """Form action for comment forms"""

    # Redirect to homepage early if HTTP method is not POST
    if request.method != "POST":
        return redirect('homepage')
    
    form = UserPostForm(request.POST)
    if form.is_valid():
        user = request.user
        text_content = form.cleaned_data.get('post_content')
        parent_post_id = request.POST.get('post-id')
        parent_post = GenericPost.objects.get(pk=parent_post_id)
        top_level_parent = parent_post.top_level_parent if parent_post.top_level_parent else parent_post
        new_post = GenericPost(author=user,
                               post_content=text_content,
                               top_level_parent=top_level_parent,
                               immediate_parent=parent_post,
                               )
        new_post.save()
        return redirect('homepage')

@login_required
def individual_post_view(request, id):
    """Returns the page for an individual post with most comments"""

    post = GenericPost.objects.get(pk=id)
    context = {
        'post': post
    }
    return render(request, 'posts/individual_post.html', context=context)
    
@login_required
def profile_view(request, id):
    user = get_object_or_404(User, pk=id)
    data = ExtendedUserData.objects.get(user=user)
    context = {
        'user': user,
        'data': data
    }
    return render(request, 'profile.html', context=context)

@login_required
def create_game_view(request):
    form = GameCreationForm()
    context = {
        'form': form
    }
    return render(request, 'creators/create_game.html', context=context)

@login_required
def game_landing_view(request, id):
    game = Game.objects.get(pk=id)
    context = {
        'game': game
    }
    return render(request, 'games/game_landing.html', context=context)

@login_required
def process_game(request):

    if request.method != "POST":
        redirect('homepage')

    form = GameCreationForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data.get('title')
        genre = form.cleaned_data.get('genre')
        blurb = form.cleaned_data.get('blurb')
        description = form.cleaned_data.get('description')
        new_game = Game(title=title,
                        genre=genre,
                        blurb=blurb,
                        description=description)
        new_game.save()
        return redirect('game_landing', id=new_game.id)

@login_required
def create_devblog_view(request):
    context = {}
    return render(request, 'creators/create_devblog.html', context=context)