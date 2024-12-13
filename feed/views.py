from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserPostForm, UserProfileDataForm
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
    current_user_extended_data = ExtendedUserData.objects.get(user=request.user.id)
    context = {
        'form': form,
        'posts': all_posts,
        'extended_user_data': current_user_extended_data,
        }
    
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
def process_follow(request):

    # This needs to be done with AJAX instead of a POST request
    
    if request.method != "POST":
        return redirect('homepage')
    
    initiating_user_id = request.POST.get('initiating_user_id')
    target_user_id = request.POST.get('target_user_id')

    initiating_user = ExtendedUserData.objects.get(user=initiating_user_id)
    target_user = User.objects.get(pk=target_user_id)

    if not initiating_user or not target_user:
        #TODO: Error out instead of redirect
        return redirect('homepage')
    
    initiating_user.followed_users.add(target_user)
    initiating_user.save()

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
    data = get_object_or_404(ExtendedUserData, user=user)
    context = {
        'user': user,
        'data': data
    }
    return render(request, 'profile/profile.html', context=context)

@login_required
def edit_profile_view(request, id):
    # Query to get the targeted user's profile data
    current_user_data = ExtendedUserData.objects.get(user=id)

    # Prevent users from editing other user's profiles
    # TODO: send 403 forbidden error instead
    if request.user.id != id:
        return redirect('homepage')
    
    if request.method == "POST":
        form = UserProfileDataForm(request.POST, request.FILES)
        if form.is_valid():
            new_headliner = form.data["headliner"]
            new_bio = form.data["bio"]
            new_location = form.data["location"]

            # Set the profile pic to uploaded pic or to 
            # whatever it was already set to if no pic was
            # provided
            try:
                new_profile_pic = form.files["profile_pic"]
            except KeyError:
                new_profile_pic = current_user_data.profile_pic

            current_user_data.headliner = new_headliner
            current_user_data.bio = new_bio
            current_user_data.location = new_location
            current_user_data.profile_pic = new_profile_pic
            current_user_data.save()
            return redirect('profile', id=current_user_data.user.id)
        
    # Construct form with default values
    form = UserProfileDataForm(initial={
        "headliner": current_user_data.headliner,
        "bio": current_user_data.bio,
        "location": current_user_data.location,
        "profile_pic": current_user_data.profile_pic
    })
    
    context = {
        'form': form
    }

    return render(request, 'profile/edit_profile.html', context=context)

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
def game_browsing_view(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'games/game_browse.html', context=context)

@login_required
def create_devblog_view(request):
    context = {}
    return render(request, 'creators/create_devblog.html', context=context)