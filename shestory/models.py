import uuid

from django.db import models


class BaseEntity(models.Model):
    """
    Это для таблиц
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class BaseReference(BaseEntity):
    """
    Это для справочников
    """
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.code} - {self.name}"


class CivilizationReference(BaseReference):
    pass


class CountryReference(BaseReference):
    civilization = models.ForeignKey(CivilizationReference, on_delete=models.CASCADE)


class RoleReference(BaseReference):
    pass


class People(BaseEntity):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField(null=True, blank=True)
    death_year = models.IntegerField(null=True, blank=True)
    country = models.ForeignKey(CountryReference, on_delete=models.CASCADE)
    roles = models.ManyToManyField(RoleReference)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    achievements = models.TextField()
    start_of_reign = models.CharField(max_length=50, null=True, blank=True)
    end_of_reign = models.CharField(max_length=50, null=True, blank=True)

    def save_form_data(self, request, instance, form, change):
            RoleReference = form.cleaned_data.get('roles')
            if RoleReference.filter(code='001').exists():
                instance.start_of_reign = form.cleaned_data.get('start_of_reign')
                instance.end_of_reign = form.cleaned_data.get('end_of_reign')
            super().save_form_data(request, instance, form, change)

    def __str__(self):
        return f"{self.id} - {self.birth_year}-{self.death_year} {self.country} - {self.nationality} - {self.achievements} - {self.end_of_reign} - {self.start_of_reign}"
