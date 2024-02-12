from rest_framework import serializers
from .models import Court


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = '__all__'  # This will include all fields from the model
