# Generated by Django 5.0.4 on 2024-04-21 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0005_player_success_games'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name': 'Player', 'verbose_name_plural': 'Players'},
        ),
    ]