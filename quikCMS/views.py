from django.shortcuts import render, redirect, get_object_or_404

from feed.models import Game
# Create your views here.
def cms_landing(request, id):
    target_game = get_object_or_404(Game, pk=id)
    if target_game:
        num_posts = target_game.posts_per_game.all().count()
        context = {
            'game': target_game,
            'num_posts': num_posts
        }
        return render(request, 'quikCMS\cms_landing.html', context=context)
    return redirect('homepage')