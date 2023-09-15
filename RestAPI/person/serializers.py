from rest_framework import serializers
from .models import person


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = "__all__"
