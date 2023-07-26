from rest_framework import serializers
from .models import Registration

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
            model=Registration
            fields='__all__'
            extra_kwargs = {'password': {'write_only': True}}