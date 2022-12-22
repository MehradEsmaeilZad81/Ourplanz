from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Profile
        fields = ['id', 'user_id', 'first_name', 'last_name', 'phone', 'birth_date', 'join_date']
