# Generated by Django 4.2.6 on 2024-05-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0002_team_lost_team_matches_team_won'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammatch',
            name='batting_overs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teammatch',
            name='batting_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teammatch',
            name='batting_wickets',
            field=models.IntegerField(default=0),
        ),
    ]
