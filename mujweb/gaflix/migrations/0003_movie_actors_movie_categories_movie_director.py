# Generated by Django 4.0.2 on 2022-02-17 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaflix', '0002_alter_actor_birth_date_alter_actor_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(blank=True, null=True, to='gaflix.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='gaflix.Category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gaflix.director'),
        ),
    ]