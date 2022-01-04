# Generated by Django 4.0 on 2022-01-04 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_review_movie_review_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.movie'),
            preserve_default=False,
        ),
    ]