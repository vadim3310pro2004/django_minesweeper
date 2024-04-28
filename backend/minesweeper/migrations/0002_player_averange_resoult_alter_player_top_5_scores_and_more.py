# Generated by Django 5.0.4 on 2024-04-20 11:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minesweeper', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='averange_resoult',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Averange game time'),
        ),
        migrations.AlterField(
            model_name='player',
            name='top_5_scores',
            field=models.JSONField(default=list, verbose_name='Best five resoults'),
        ),
        migrations.AlterField(
            model_name='player',
            name='total_games',
            field=models.PositiveIntegerField(default=0, verbose_name='Total games'),
        ),
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='player', to=settings.AUTH_USER_MODEL, verbose_name='Id in User table'),
        ),
    ]
