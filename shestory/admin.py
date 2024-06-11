from django.contrib import admin
from .models import CivilizationReference, CountryReference, RoleReference, People


@admin.register(CivilizationReference)
class CivilizationReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(CountryReference)
class CountryReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(RoleReference)
class RoleReferenceAdmin(admin.ModelAdmin):
    pass


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birth_year', 'death_year', 'country', 'nationality', 'achievements')  # Поля, отображаемые в списке
    list_filter = ('country', 'nationality')  # Фильтры для списка
    search_fields = ('name', 'nationality')  # Поля для поиска
    fields = ('name', 'birth_year', 'death_year', 'country', 'nationality', 'roles', 'start_of_reign', 'end_of_reign',
              'achievements')  # Добавлены новые поля
