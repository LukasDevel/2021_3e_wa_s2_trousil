# Generated by Django 4.0.2 on 2022-03-24 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaflix', '0003_movie_actors_movie_categories_movie_director'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='actor',
            name='sex',
            field=models.CharField(choices=[('male', 'Muž'), ('female', 'Žena'), ('other', 'Ostatní')], default='male', max_length=32),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, to='gaflix.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, to='gaflix.Category'),
        ),
    ]
