from django.contrib import admin

from pokemon_entities.models import Pokemon, PokemonEntity, PokemonElementType


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass


@admin.register(PokemonEntity)
class PokemonEntityAdmin(admin.ModelAdmin):
    pass


@admin.register(PokemonElementType)
class PokemonElementTypeAdmin(admin.ModelAdmin):
    pass
