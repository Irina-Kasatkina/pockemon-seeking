# Generated by Django 3.1.14 on 2022-08-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='default description'),
            preserve_default=False,
        ),
    ]