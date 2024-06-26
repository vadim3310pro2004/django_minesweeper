# Generated by Django 5.0.4 on 2024-04-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0008_alter_player_success_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='averange_resoult',
            field=models.FloatField(blank=True, null=True, verbose_name='Averange game time'),
        ),
        migrations.AlterField(
            model_name='player',
            name='success_games',
            field=models.PositiveIntegerField(default=0, verbose_name='Success games'),
        ),
    ]
