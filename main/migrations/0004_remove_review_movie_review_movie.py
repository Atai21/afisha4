# Generated by Django 4.0 on 2022-01-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ManyToManyField(to='main.Movie'),
        ),
    ]
