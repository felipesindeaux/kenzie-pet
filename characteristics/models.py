from django.db import models


class Characteristic(models.Model):
    name = models.CharField(max_length=20, unique=True)

    animals = models.ManyToManyField("animals.Animal", related_name='characteristics')

    def __repr__(self) -> str:
        return f'Characteristic {self.id} - {self.name}'
