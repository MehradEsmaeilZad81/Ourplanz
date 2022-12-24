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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'plans_count', 'plans']

    plans = serializers.SerializerMethodField(method_name='get_plans')
    plans_count = serializers.SerializerMethodField(method_name='get_plans_count')

    def get_plans(self, tag: Tag):
        plans = []
        for p in tag.plan_set.all():
            plans.append(p.title)
        return plans

    def get_plans_count(self, tag: Tag):
        return tag.plan_set.all().count()
