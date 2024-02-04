from rest_framework import serializers
from .models import Court


class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ('courtID', 'num_availability',
                  'availabilityTag', 'address', 'court_image')
