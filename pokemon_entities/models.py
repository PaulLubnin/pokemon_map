from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField('Название на русском', max_length=200, blank=False, null=False)
    title_en = models.CharField('Название на английском', max_length=200, blank=True, null=False)
    title_jp = models.CharField('Название на японском', max_length=200, blank=True, null=False)
    image = models.ImageField('Изображение', blank=True, null=True)
    description = models.TextField('Описание', blank=True, null=False)
    previous_evolution = models.ForeignKey('self', verbose_name='Из кого эволюционировал', on_delete=models.CASCADE,
                                           related_name='next_evolution', blank=True, null=True)

    class Meta:
        verbose_name = 'Покемон'
        verbose_name_plural = 'Покемоны'

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='Покемон', on_delete=models.CASCADE, blank=False, null=True)
    lat = models.FloatField('Широта', blank=True, null=True)
    lon = models.FloatField('Долгота', blank=True, null=True)
    appeared_at = models.DateTimeField('Появление', blank=True, null=True)
    disappeared_at = models.DateTimeField('Исчезновение', blank=True, null=True)
    level = models.IntegerField('Уровень', blank=True, null=True)
    health = models.IntegerField('Здоровье', blank=True, null=True)
    strength = models.IntegerField('Сила', blank=True, null=True)
    defence = models.IntegerField('Защита', blank=True, null=True)
    stamina = models.IntegerField('Энергия', blank=True, null=True)

    class Meta:
        verbose_name = 'Сущность покемона'
        verbose_name_plural = 'Сущности покемонов'

    def __str__(self):
        return f'{self.pokemon.title_ru}({self.id})'
