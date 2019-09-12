from .models import Duck
from rest_framework import serializers

class DuckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Duck
        fields = ('id', 'duck_name', 'duck_last_name', 'duck_mail', 'duck_age')