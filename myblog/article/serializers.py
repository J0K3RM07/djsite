from rest_framework import serializers
from .models import article

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = ('title', 'date')
