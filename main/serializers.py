from rest_framework import serializers
from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['title', 'description', 'created_at', 'updated_at', 'starts_at', 'limit', 'tags', 'mentor']

    tags = serializers.SerializerMethodField(method_name='get_tags')

    def get_tags(self, plan: Plan):
        tags = []
        for t in plan.tags.all():
            tags.append(t.title)
        return tags
