from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializers import ItemSerializer
from rest_framework import serializers, status


# Create your views here.
@api_view(['GET'])
def PersonOverview(request):
    api_urls = {
        'persons': '/',
        'Search by full_name': '/?full_name=full_name',
        'Search by slack_name': '/?slack_name=slack_name',
        'Search by track': '/?track=track',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)


# Create a person instance
@api_view(['POST'])
def create_person(request):
    person = ItemSerializer(data=request.data)

    # validate if person full_name already exist
    if Person.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if person.is_valid():
        person.save()
        return Response(person.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

#Fetch all persons in the database
@api_view(['GET'])
def view_persons(request):
    # checking for the parameters from the URL
    if request.query_params:
        persons = Person.objects.filter(**request.query_params.dict())
    else:
        persons = Person.objects.all()

    # if there is something in items else raise error
    if persons:
        serializer = ItemSerializer(persons, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#Update person using pk
@api_view(['POST'])
def update_person(request, pk):
    person = Person.objects.get(pk=pk)
    data = ItemSerializer(instance=person, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


#Delete person from database
@api_view(['DELETE'])
def delete_person(request, pk):
    person = Person.objects.get(pk=pk)
    person.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
