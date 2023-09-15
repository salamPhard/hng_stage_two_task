from django.db.models import fields
from rest_framework import serializers
from .models import Person


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('full_name', 'slack_name', 'track')