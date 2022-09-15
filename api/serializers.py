from dataclasses import field
from rest_framework import serializers
from .models import Apipost


class ApiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Apipost
        fields = '__all__'