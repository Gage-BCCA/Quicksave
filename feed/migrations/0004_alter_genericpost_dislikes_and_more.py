# Generated by Django 5.1.4 on 2024-12-09 14:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_keyword_remove_userpostlikes_post_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpost',
            name='dislikes',
            field=models.ManyToManyField(default=None, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='genericpost',
            name='keywords',
            field=models.ManyToManyField(default=None, to='feed.keyword'),
        ),
        migrations.AlterField(
            model_name='genericpost',
            name='likes',
            field=models.ManyToManyField(default=None, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
