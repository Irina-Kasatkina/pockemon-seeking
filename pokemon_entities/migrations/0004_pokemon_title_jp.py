# Generated by Django 3.1.14 on 2022-08-26 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_pokemon_title_en'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='title_jp',
            field=models.CharField(default='default title_jp', max_length=200),
            preserve_default=False,
        ),
    ]
