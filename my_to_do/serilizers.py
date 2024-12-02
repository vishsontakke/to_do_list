from .models import Todolist
from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

class TodolistSerilizer(HyperlinkedModelSerializer):
    class Meta:
        model = Todolist
        fields = ['url', 'id', 'title', 'discription', 'is_completed']
        