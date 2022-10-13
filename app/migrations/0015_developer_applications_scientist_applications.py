# Generated by Django 4.0.4 on 2022-06-30 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_applicationcomponent_applications'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='applications',
            field=models.ManyToManyField(blank=True, to='app.application'),
        ),
        migrations.AddField(
            model_name='scientist',
            name='applications',
            field=models.ManyToManyField(blank=True, to='app.application'),
        ),
    ]
