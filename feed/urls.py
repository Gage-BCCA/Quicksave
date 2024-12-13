from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage_view, name='homepage'),

    # Processing URLs
    path('process-post/', views.process_post, name="process_post"),
    path('process-comment/', views.process_comment, name="process_comment"),
    path('process_game/', views.process_game, name="process_game"),
    path('process_follow/', views.process_follow, name="process_follow"),

    # Post URLs
    path('p/<int:id>', views.individual_post_view, name="individual_post"),

    # Non-authentication related user URLs
    path('u/<int:id>', views.profile_view, name="profile"),
    path('u/<int:id>/edit-profile', views.edit_profile_view, name="edit_profile"),
    
    # Game URLs
    path('g/create', views.create_game_view, name="create_game"),
    path('g/browse', views.game_browsing_view, name="game_browse"),
    path('g/<int:id>', views.game_landing_view, name="game_landing")
]