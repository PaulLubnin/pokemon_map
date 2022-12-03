# Generated by Django 3.1.14 on 2022-10-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20221020_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonElementType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35, verbose_name='Стихия покемона')),
            ],
            options={
                'verbose_name': 'Стихия покемона',
                'verbose_name_plural': 'Стихии покемонов',
            },
        ),
        migrations.AddField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType'),
        ),
    ]
