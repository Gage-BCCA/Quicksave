from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),

    # Processing URLs
    path('process-post/', views.process_post, name="process_post"),
    path('process-comment/', views.process_comment, name="process_comment"),
    path('process-game/', views.process_game, name="process_game"),
    path('process-follow_user/', views.process_follow, name="process_follow"),
    path('process-follow-game/', views.process_follow_game, name="process_follow_game"),
    path('process-post-like/', views.process_post_like, name="process_post_like"),
    path('process-post-dislike/', views.process_post_dislike, name="process_post_dislike"),

    # Post URLs
    path('p/<int:id>', views.individual_post_view, name="individual_post"),
    path('p/create', views.create_post_view, name="create_post"),

    # Non-authentication related user URLs
    path('u/<int:id>', views.profile_view, name="profile"),
    path('u/<int:id>/edit', views.edit_profile_view, name="edit_profile"),
    
    # Game URLs
    path('g/create', views.create_game_view, name="create_game"),
    path('g/browse', views.game_browsing_view, name="game_browse"),
    path('g/<int:id>', views.game_landing_view, name="game_landing"),
    path('g/<int:id>/edit', views.game_edit_view, name="game_edit"),
]