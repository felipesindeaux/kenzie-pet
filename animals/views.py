from urllib import request

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalsView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)
    
    def post(self, request):

        serializer = AnimalSerializer(data={**request.data})

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    

class AnimalViewById(APIView):
    def get(self, request, id):

        try:
            animal = Animal.objects.get(pk=id)
            serializer = AnimalSerializer(animal)
            return Response(serializer.data)
        except Animal.DoesNotExist:
            return Response({'message': 'Animal not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            animal = Animal.objects.get(pk=id)
            animal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Animal.DoesNotExist:
            return Response({'message': 'Animal not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, id):

        if request.data.get('sex', None):
            return Response({'message': f'You can not update sex property.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        if request.data.get('group'):
            return Response({'message': f'You can not update group property.'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        try:
            animal = Animal.objects.get(pk=id)
            serializer = AnimalSerializer(animal, request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            return Response(serializer.data)

        except Animal.DoesNotExist:
            return Response({'message': 'Animal not found'}, status=status.HTTP_404_NOT_FOUND)
