from django.core.management.base import BaseCommand, CommandError

from django.contrib.auth.models import User
from accounts.models import ExtendedUserData
from feed.models import Genre, Game, GenericPost

from faker import Faker

import random

class Command(BaseCommand):
    help = "Generates 25 random users, 5 random games, 4 generic genres, and 100 posts on random games."


    def handle(self, *args, **options):
        fake = Faker()

        # Create 25 Users
        for _ in range(25):
            new_user = User.objects.create(
                username=fake.user_name(),
                password=fake.password(),
                email=fake.email()
            )
            new_user.save()
            new_user_data = ExtendedUserData(
                user=new_user,
                headliner=fake.sentence(nb_words=10),
                bio=fake.text(max_nb_chars=200)
            )
            new_user_data.save()

        # Create 4 Random Genres
        genres = ["Action", "Shooter", "Casual", "Strategy"]
        for genre in genres:
            new_genre = Genre(
                genre=genre
            )
            new_genre.save()

        # Create 5 Games
        for _ in range(5):
            game = Game.objects.create(
                title=fake.catch_phrase(),
                genre=Genre.objects.get(pk=random.randint(1,4)),
                blurb=fake.bs(),
                description=fake.text(max_nb_chars=255),
                price=random.random(),
            )
            game.save()
            game.developers.add(User.objects.get(pk=random.randint(1, 24)))
        
        # Create 25 Posts with 4 comments each
        for _ in range(25):
            related_game = Game.objects.get(pk=random.randint(1,5))
            post = GenericPost(
                post_content = fake.text(max_nb_chars=500),
                top_level_parent = None,
                immediate_parent = None,
                author = User.objects.get(pk=random.randint(1, 24)),
                related_game=related_game
            )
            post.save()

            # Generate Comments to Top Level Posts
            for _ in range(5):
                comment_depth_1 = GenericPost(
                    post_content = fake.text(max_nb_chars=500),
                    top_level_parent = post,
                    immediate_parent = post,
                    author = User.objects.get(pk=random.randint(1, 24)),
                    related_game=related_game
                    )
                comment_depth_1.save()

                # Generate Responses to Depth 1 Comments
                for _ in range(random.randint(1, 3)):
                    comment_depth_2 = GenericPost(
                        post_content = fake.text(max_nb_chars=500),
                        top_level_parent = post,
                        immediate_parent = comment_depth_1,
                        author = User.objects.get(pk=random.randint(1, 24)),
                        related_game=related_game
                        )
                    comment_depth_2.save()
    
        self.stdout.write(self.style.SUCCESS('Successfully generated dummy data'))