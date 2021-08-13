from django.db import models
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta

from api.models import Deal


class DealFileSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ('file', )


class ClientsSerializer(serializers.Serializer):
    username = serializers.CharField()
    spent_money = serializers.IntegerField()
    gems = serializers.ListField()

    class Meta:
        fields = ('username', 'spent_money', 'gems', )