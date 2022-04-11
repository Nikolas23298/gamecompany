# Generated by Django 4.0.3 on 2022-04-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_game_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='header_image',
        ),
        migrations.AddField(
            model_name='game',
            name='game_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]