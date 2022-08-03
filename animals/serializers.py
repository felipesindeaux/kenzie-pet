from characteristics.models import Characteristic
from characteristics.serializers import CharacteristicSerializer
from groups.models import Group
from groups.serializers import GroupSerializer
from rest_framework import serializers

from animals.models import Animal


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)
    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data):

        characteristics = validated_data.pop('characteristics')

        validated_characteristics = [Characteristic.objects.get_or_create(**char)[0] for char in characteristics]

        try:
            group = Group.objects.get(name=validated_data['group']['name'])
        
        except Group.DoesNotExist:
            group = Group.objects.create(**validated_data['group'])

        new_data = {**validated_data, 'group': group}

        created_animal = Animal.objects.create(**new_data)

        for char in validated_characteristics:
            char.animals.add(created_animal)

        return created_animal

    def update(self, instance, validated_data):

        if validated_data.get('characteristics', None):

            new_characteristics = validated_data.pop('characteristics')
            old_characteristics = instance.characteristics.all()

            validated_characteristics = [Characteristic.objects.get_or_create(**char)[0] for char in new_characteristics]

            instance.characteristics.set([*old_characteristics, *validated_characteristics])

        for key, value in validated_data.items():
            setattr(instance, key, value)
            
        instance.save()


        return instance
