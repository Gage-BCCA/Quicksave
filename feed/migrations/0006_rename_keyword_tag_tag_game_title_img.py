# Generated by Django 5.1.4 on 2024-12-13 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_genre_tag_game'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='keyword',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='game',
            name='title_img',
            field=models.ImageField(null=True, upload_to='games/title-img/'),
        ),
    ]